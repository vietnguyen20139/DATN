#include <DHT.h>
// #include <DHT_U.h>
// #include <Arduino.h>
#include <U8g2lib.h>
// #include <U8x8lib.h>
#include <Wire.h>
#include <TimeLib.h>
#include <Keypad.h>
#include <Arduino_FreeRTOS.h>
#include <TinyGPSPlus.h>
// #include <SPI.h>
#include <SD.h>

// Address DS1307 (RTC)
const byte DS1307 = 0x68;
const byte NumberOfFields = 7;

const char DEGREE_SYMBOL[] = { 0xB0, '\0' };

// LCD setup                            clock-data-CS-reset
U8G2_ST7920_128X64_1_SW_SPI u8g2(U8G2_R0, 13, 11, 10, 8);
const char *dayNames[] = { "", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" };

// Keypad setup
const byte ROWS = 4;
const byte COLS = 3;
char keys[ROWS][COLS] = {
  { '1', '2', '3' }, { '4', '5', '6' }, { '7', '8', '9' }, { '*', '0', '#' }
};
byte rowPins[ROWS] = { 9, 8, 7, 6 };
byte colPins[COLS] = { 5, 4, 3 };
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

// Khai báo các biến thời gian
int rtcSecond, rtcMinute, rtcHour, rtcDay, rtcWday, rtcMonth, rtcYear;

// Global variable for RTC
char timeString[9];   // format: HH:MM:SS
char dateString[11];  // format: DD/MM/YYYY
char dayString[9];    // Day of the week

String input = "";
String maskedInput = "";
bool passwordMode = false;
bool loggedIn = false;  // Track login status

int tiltX = 0;
int tiltY = 0;
int tiltZ = 0;
// float vibrationMagnitude = 0;
int levelVib = 0;

// Khai báo các hằng số và biến cần thiết
const int xPin = A0;
const int xMin = 278;
const int xMax = 412;

const int yPin = A1;
const int yMin = 274;
const int yMax = 410;

const int zPin = A2;
const int zMin = 275;
const int zMax = 413;

//GPS
// The TinyGPSPlus object
TinyGPSPlus gps;

float ute_lat = 10.849820;
float ute_lng = 106.772171;

String orderIDStr = "2013904925";
String FIREBASE_HOST = "https://datn-43437-default-rtdb.asia-southeast1.firebasedatabase.app/orders/" + orderIDStr + "/datas";
String FIREBASE_HOST_END = "https://datn-43437-default-rtdb.asia-southeast1.firebasedatabase.app/orders/" + orderIDStr + "/complete";
const String FIREBASE_SECRET = "4odFwAJHDuVD2lPXSBYaXqcVk9y0crhe0pXSSuO4";

int numstop = 2;
int distance = 500;  //m
String coordinates[] = { "10.850697,106.772072", "10.845097,106.79685"};
// Password setup
String topPass = "0000";
String yourPassword[] = { "1111", "2222" };

float lat = 10.850697, lng = 106.772072;
int speed = 0;

int isToLocation[] = { 0, 0 };
int EndAllToLocation[] = { 0, 0 };

// String coordinates[] = { "10.850275,106.772099", "10.850275,106.772099" };
// Global variables for GPS data
String data;

String idString;
unsigned int ID = 0;

int DELAY_MS = 500;

#define DHTTYPE DHT22
unsigned long delayTime;
uint8_t DHTPin = 62;
DHT dht(DHTPin, DHTTYPE);
int Temperature;
int Humidity;

// Function declarations
void readDS1307(void *pvParameters);
void handleKeypad(void *pvParameters);
void acceTask(void *pvParameters);
void dhtTask(void *pvParameters);

void passwordDisplay();
void digitalClockDisplay();
void displayTemperatureAndHumidity();
void printDigits(int digits);
void setTime(byte hr, byte min, byte sec, byte wd, byte d, byte mth, byte yr);
void setTimeFromCompile();
int bcd2dec(byte num);
int dec2bcd(byte num);
void gpsTask(void *pvParameters);
void smartDelay(unsigned long ms);
void init_gsm();
void post_to_firebase(String data);
bool waitResponse(String expected_answer = "OK", unsigned int timeout = 2000);

void setup() {
  Wire.begin();
  Serial.begin(9600);
  u8g2.begin();

  pinMode(DHTPin, INPUT);
  dht.begin();
  Serial3.begin(9600);

  Serial1.begin(115200);

  // Create FreeRTOS tasks
  xTaskCreate(readDS1307, "ReadDS1307", 384, NULL, 1, NULL);
  xTaskCreate(handleKeypad, "HandleKeypad", 512, NULL, 1, NULL);
  xTaskCreate(acceTask, "Acce Task", 384, NULL, 1, NULL);
  xTaskCreate(dhtTask, "DHT Task", 384, NULL, 1, NULL);
  xTaskCreate(gpsTask, "GPS Task", 1536, NULL, 2, NULL);


  // Start the scheduler
  vTaskStartScheduler();
}

void loop() {
  // Empty loop because using FreeRTOS tasks
}

// delay task 60s
void dhtTask(void *pvParameters) {
  // (void)pvParameters;

  while (1) {
    Serial.println(F("dht task"));
    Humidity = dht.readHumidity();
    Temperature = dht.readTemperature();

    if (!isnan(Humidity) && !isnan(Temperature)) {
      // Serial.print(F("Humidity: "));
      // Serial.print(Humidity);
      // Serial.print(F("%  Temperature: "));
      // Serial.print(Temperature);
      // Serial.println(F("°C "));
    } else {
      Serial.println(F("Failed to read from DHT sensor!"));
    }

    vTaskDelay(60000 / portTICK_PERIOD_MS);  // delay task 60s
  }
}

// delay task 800ms
void acceTask(void *pvParameters) {
  // (void)pvParameters;

  float lastXAcc = 0;
  float lastYAcc = 0;
  float lastZAcc = 0;

  while (1) {
    Serial.println(F("adxl task"));

    int xVal = analogRead(xPin);
    int yVal = analogRead(yPin);
    int zVal = analogRead(zPin);

    // Tính gia tốc theo các trục
    float xAcc = abs((float)(xVal - xMin) / (xMax - xMin) * 2 - 1);
    float yAcc = abs((float)(yVal - yMin) / (yMax - yMin) * 2 - 1);
    float zAcc = abs((float)(zVal - zMin) / (zMax - zMin) * 2 - 1);

    // Tính tổng sự thay đổi của các trục
    float deltaAcc = abs(xAcc - lastXAcc) + abs(yAcc - lastYAcc) + abs(zAcc - lastZAcc);
    if (deltaAcc > 1 && deltaAcc < 2) {
      levelVib = 2;
    } else if (deltaAcc > 2) {
      levelVib = 3;
    } else {
      levelVib = 1;
    }

    // Cập nhật giá trị lần trước của các trục
    lastXAcc = xAcc;
    lastYAcc = yAcc;
    lastZAcc = zAcc;

    // Tính tổng gia tốc
    // vibrationMagnitude = sqrt(xAcc * xAcc + yAcc * yAcc + zAcc * zAcc);

    // Tính góc nghiêng theo từng trục
    tiltX = calculateTilt(xAcc);
    tiltY = calculateTilt(yAcc);
    tiltZ = calculateTilt(zAcc);

    // In ra Serial Monitor
    // Serial.print("Độ rung lắc: ");
    // Serial.println(deltaAcc);

    // Serial.print("Độ nghiêng theo trục Y: ");
    // printTilt(tiltY);

    // Serial.print("Độ nghiêng theo trục X: ");
    // printTilt(tiltX);

    // Serial.print("Độ nghiêng theo trục Z: ");
    // printTilt(tiltZ);

    vTaskDelay(800 / portTICK_PERIOD_MS);  // delay task 800ms
  }
}

// delay task 1000ms
void readDS1307(void *pvParameters) {
  setTimeFromCompile();

  while (1) {
    Serial.println(F("readDS1307 task"));

    Wire.beginTransmission(DS1307);
    Wire.write((byte)0x00);
    Wire.endTransmission();
    Wire.requestFrom(DS1307, NumberOfFields);

    rtcSecond = bcd2dec(Wire.read() & 0x7f);
    rtcMinute = bcd2dec(Wire.read());
    rtcHour = bcd2dec(Wire.read() & 0x3f);
    rtcWday = bcd2dec(Wire.read());
    rtcDay = bcd2dec(Wire.read());
    rtcMonth = bcd2dec(Wire.read());
    rtcYear = bcd2dec(Wire.read());
    rtcYear += 2000;

    char id[20];
    sprintf(id, "%04d%02d%02d%02d%02d%02d", rtcYear, rtcMonth, rtcDay, rtcHour, rtcMinute, rtcSecond);

    idString = String(id);
    digitalClockDisplay();
    // if (passwordMode == true) {
    //   passwordDisplay();
    // }
    // if (passwordMode == false) {
    //   displayTemperatureAndHumidity();
    // }
    vTaskDelay(1000 / portTICK_PERIOD_MS);  // delay task 1000ms
  }
}

// delay 100ms
void handleKeypad(void *pvParameters) {
  while (1) {
    Serial.println(F("keypad task"));

    char key = keypad.getKey();
    if (passwordMode == true) {
      passwordDisplay();
    }
    if (passwordMode == false) {
      displayTemperatureAndHumidity();
    }

    if (key != NO_KEY) {
      // if (passwordMode == 0) {
      if (key != '*') {
        passwordMode = true;
        if (key == '#') {

          if (input == topPass) {
            loggedIn = true;
            passwordMode = false;
          } else {

            for (int i = 0; i < numstop; i++) {
              if (input == yourPassword[i]) {
                // check if go to location
                if (isToLocation[i]) {
                  // if pass correct and is in correct location, then EndAllToLocation at location i is set 1
                  EndAllToLocation[i] = 1;
                  Serial.println(input);
                  loggedIn = true;
                  passwordMode = false;
                  break;
                }
                // delay(500);
              } else {
                passwordMode = false;
                loggedIn = false;
              }
            }
          }
          if (loggedIn) {
            u8g2.firstPage();
            do {
              u8g2.clearBuffer();
              u8g2.setFont(u8g2_font_ncenB08_tr);
              u8g2.drawStr(0, 24, "Correct password");
            } while (u8g2.nextPage());

            // delay 500ms to see
            // unsigned long startTime = millis();
            // unsigned long delayTime = 500;
            // while (millis() - startTime < delayTime) {
            // }
            TickType_t startTick = xTaskGetTickCount();
            TickType_t waitTicks = pdMS_TO_TICKS(500);  // 1000 ms wait

            while (xTaskGetTickCount() - startTick < waitTicks) {
              // Optionally do something else or just spin
            }
          } else {
            u8g2.firstPage();
            do {
              u8g2.clearBuffer();
              u8g2.setFont(u8g2_font_ncenB08_tr);
              u8g2.drawStr(0, 24, "Incorrect password");
            } while (u8g2.nextPage());

            // delay 500ms to see
            // unsigned long startTime = millis();
            // unsigned long delayTime = 500;
            // while (millis() - startTime < delayTime) {
            // }
            TickType_t startTick = xTaskGetTickCount();
            TickType_t waitTicks = pdMS_TO_TICKS(500);  // 1000 ms wait

            while (xTaskGetTickCount() - startTick < waitTicks) {
              // Optionally do something else or just spin
            }
          }

          input = "";
          maskedInput = "";
        } else {
          input += key;
          maskedInput += '*';
        }
      } else {
      }
      // }
      //passwordDisplay();
    }

    vTaskDelay(100 / portTICK_PERIOD_MS);
  }
}

// SUB-FUNCTION
void passwordDisplay() {
  u8g2.firstPage();
  do {
    u8g2.clearBuffer();
    // Hiển thị mật khẩu nếu đang ở chế độ nhập mật khẩu
    if (passwordMode) {
      u8g2.setFont(u8g2_font_ncenB08_tr);
      u8g2.drawStr(0, 24, "Enter your password");
      u8g2.drawStr(0, 38, maskedInput.c_str());
    }
    // Luôn hiển thị thời gian
    u8g2.setFont(u8g2_font_4x6_tr);
    u8g2.drawStr(0, 5, dayString);
    u8g2.drawStr(36, 5, timeString);
    u8g2.drawStr(72, 5, dateString);

  } while (u8g2.nextPage());
}

void digitalClockDisplay() {
  // Cập nhật các biến toàn cục cho thời gian, ngày và ngày trong tuần
  sprintf(timeString, "%02d:%02d:%02d", rtcHour, rtcMinute, rtcSecond);
  sprintf(dateString, "%02d/%02d/%04d", rtcDay, rtcMonth, rtcYear);
  strcpy(dayString, dayNames[rtcWday]);

  // Serial.println(timeString);
  // Serial.println(dateString);
  // Serial.println(dayString);
}

void displayTemperatureAndHumidity() {

  char tempString[5];
  char humString[5];
  char tiltXStr[5];
  char tiltYStr[5];
  char tiltZStr[5];
  char levelVibStr[5];
  char tiltSpeedStr[5];

  // Chuyển đổi giá trị nhiệt độ và độ ẩm từ kiểu int sang chuỗi ký tự
  sprintf(tempString, "%d", Temperature);
  sprintf(humString, "%d", Humidity);
  sprintf(tiltXStr, "%d", tiltX);
  sprintf(tiltYStr, "%d", tiltY);
  sprintf(tiltZStr, "%d", tiltZ);
  sprintf(levelVibStr, "%d", levelVib);
  sprintf(tiltSpeedStr, "%d", speed);

  u8g2.firstPage();
  do {
    u8g2.clearBuffer();
    // Hiển thị nhiệt độ và độ ẩm
    u8g2.drawFrame(0, 0, 128, 12);
    u8g2.setFont(u8g2_font_resoledbold_tr);
    u8g2.drawStr(0, 23, "Temp:");
    u8g2.drawStr(34, 23, tempString);
    u8g2.setFont(u8g2_font_ncenB10_tf);
    u8g2.drawUTF8(44, 27, DEGREE_SYMBOL);
    u8g2.setFont(u8g2_font_resoledbold_tr);
    u8g2.drawUTF8(50, 23, "C");

    u8g2.drawStr(73, 23, "Hum:");
    u8g2.drawStr(100, 23, humString);
    u8g2.drawStr(114, 23, "%");

    u8g2.drawStr(0, 35, "Speed:");
    u8g2.drawStr(45, 35, tiltSpeedStr);

    u8g2.drawStr(0, 48, "Tilt:");

    u8g2.drawStr(41, 48, "X:");
    u8g2.drawStr(52, 48, tiltXStr);

    u8g2.drawStr(72, 48, "Y:");
    u8g2.drawStr(83, 48, tiltYStr);

    u8g2.drawStr(103, 48, "Z:");
    u8g2.drawStr(115, 48, tiltZStr);

    u8g2.drawStr(0, 60, "Vibration level:");
    u8g2.drawStr(97, 60, levelVibStr);

    // Luôn hiển thị thời gian
    u8g2.setFont(u8g2_font_threepix_tr);

    // u8g2.setFont(u8g2_font_4x6_tr);
    u8g2.drawStr(7, 8, dayString);
    u8g2.drawStr(43, 8, timeString);
    u8g2.drawStr(80, 8, dateString);
  } while (u8g2.nextPage());
}

void printDigits(int digits) {
  // Serial.print(":");
  if (digits < 10) {}
  // Serial.print('0');
  // Serial.print(digits);
}

void setTime(byte hr, byte min, byte sec, byte wd, byte d, byte mth, byte yr) {
  Wire.beginTransmission(DS1307);
  Wire.write(byte(0x00));
  Wire.write(dec2bcd(sec));
  Wire.write(dec2bcd(min));
  Wire.write(dec2bcd(hr));
  Wire.write(dec2bcd(wd));
  Wire.write(dec2bcd(d));
  Wire.write(dec2bcd(mth));
  Wire.write(dec2bcd(yr));
  Wire.endTransmission();
}

void setTimeFromCompile() {
  const char monthNames[] = "JanFebMarAprMayJunJulAugSepOctNovDec";
  char monthStr[4] = "";
  int hr, min, sec, d, y;
  sscanf(__TIME__, "%d:%d:%d", &hr, &min, &sec);
  sscanf(__DATE__, "%s %d %d", monthStr, &d, &y);

  int mth = (strstr(monthNames, monthStr) - monthNames) / 3 + 1;

  tmElements_t tm;
  tm.Day = d;
  tm.Month = mth;
  tm.Year = y - 1970;
  tm.Hour = hr;
  tm.Minute = min;
  tm.Second = sec;
  time_t t = makeTime(tm);
  int wd = weekday(t);

  setTime(hr, min, sec, wd, d, mth, y - 2000);
}

int bcd2dec(byte num) {
  return ((num / 16 * 10) + (num % 16));
}

int dec2bcd(byte num) {
  return ((num / 10 * 16) + (num % 10));
}

//subfunction adlx335
float calculateTilt(float acc) {
  if (acc <= -1) {
    return -90;
  } else if (acc >= 1) {
    return 90;
  } else {
    return atan2(acc, sqrt(1 - acc * acc)) * 180 / PI;
  }
}

void printTilt(float tilt) {
  if (isnan(tilt)) {
    // Serial.println("NaN");
  } else {
    // Serial.print(tilt);
    // Serial.println(" độ");
  }
}

//delay task 10s
//GPS sim and subfunction
void gpsTask(void *pvParameters) {
  // (void)pvParameters;

  while (1) {  // Get GPS data every 1 second
    Serial.println(F("GPS task"));
    
    u8g2.firstPage();
    do {
      u8g2.clearBuffer();
      u8g2.setFont(u8g2_font_ncenB08_tr);
      u8g2.drawStr(0, 24, "Send data...");
    } while (u8g2.nextPage());

    if (ID > 20000) {
      ID = 0;
    }
    smartDelay(2000);
    if (gps.location.isValid()) {
      lat = gps.location.lat();
      lng = gps.location.lng();
    }

    if (gps.speed.isValid()) {
      speed = gps.speed.kmph();
    }

    // float distToCoord = TinyGPSPlus::distanceBetween(lat, lng, coordLat, coordLon);

    // unsigned long distanceMToUTE = (unsigned long)TinyGPSPlus::distanceBetween(
    //   gps.location.lat(),
    //   gps.location.lng(),
    //   ute_lat,
    //   ute_lng);  // meters

    Serial.print(F("lat: "));
    // Get 6 digits after ".", example: 10.831239
    Serial.print(lat, 6);
    Serial.print(F(" ,lng: "));
    Serial.print(lng, 6);
    Serial.print(F(" ,speed: "));
    Serial.print(speed);
    // Serial.print(" ,distanceMToUTE: ");
    // Serial.print(distanceMToUTE);
    // Serial.println();
    for (int i = 0; i < numstop; i++) {
      float coordLat = 0;
      float coordLon = 0;
      int commaIndex = coordinates[i].indexOf(',');
      if (commaIndex != -1) {
        String latString = coordinates[i].substring(0, commaIndex);
        String lonString = coordinates[i].substring(commaIndex + 1);
        // Serial.println(latString);
        // Serial.println(lonString);

        coordLat = latString.toFloat();
        coordLon = lonString.toFloat();
        // Serial.println(coordLat, 6);
        // Serial.println(coordLon, 6);

        // Rest of your code
      }
      // Serial.print();
      float distToCoord = TinyGPSPlus::distanceBetween(lat, lng, coordLat, coordLon);

      if (distToCoord < distance) {
        isToLocation[i] = 1;
        // EndAllToLocation[i] = 1;
      } else {
        isToLocation[i] = 0;
      }

      // Print distance and if500 values for each coordinate
      // Serial.print("Distance to coordinate ");
      Serial.println();
      Serial.print(i);
      Serial.print(": ");
      Serial.print(distToCoord);
      Serial.print(F(" meters. isToLocation["));
      Serial.print(i);
      Serial.print(F("]: "));
      Serial.println(isToLocation[i]);
    }

    ++ID;
    data = String("{\"data\":\"") + idString + String(",") + String(speed) + String(",") + String(lat, 6) + String(",") + String(lng, 6) + String(",") + String(Temperature) + String(",") + String(Humidity) + String("\"}");
    // data = String("{\"data\":\"") + String(ID) + String(",") + String(speed) + String(",") + String(lat, 6) + String(",") + String(lng, 6) + String(",") + String(Temperature) + String(",") + String(Humidity) + String("\"}");
    // Serial.println(data);
    bool isAllEnd = true;
    for (int i = 0; i < numstop; i++) {
      Serial.print(F("EndAllToLocation is: "));
      Serial.println(EndAllToLocation[i]);
      if (EndAllToLocation[i] == 0) {
        isAllEnd = false;
        break;
      }
    }

    Serial.println(isAllEnd);

    if (isAllEnd) {
      Serial.println(F("end host"));
      post_to_firebase(data, FIREBASE_HOST_END);
    } else {
      Serial.println(F("base host"));
      post_to_firebase(data, FIREBASE_HOST);
    }

    Serial.println(F("send data"));
    File recordData = SD.open("data.txt", FILE_WRITE);
    if (recordData) {
      recordData.println(data);
      recordData.close();
    } else {
      // Serial.println(F("error opening data.txt"));
    }
    //   // delay_ms(5000);


    vTaskDelay(10000 / portTICK_PERIOD_MS);  //delay task 10s
  }
}

void smartDelay(unsigned long ms) {
  // unsigned long start = millis();
  TickType_t startTick = xTaskGetTickCount();
  TickType_t waitTicks = pdMS_TO_TICKS(ms);  // 1000 ms wait

  do {
    while (Serial3.available())  // Use SoftwareSerial to read from GPS module
      gps.encode(Serial3.read());
    // } while (millis() - start < ms);
  } while (xTaskGetTickCount() - startTick < waitTicks);
}

void delay_ms(unsigned long delayTime) {
  // unsigned long startTime = millis();  // Store the start time

  // while (millis() - startTime < delayTime) {
  //   // Do nothing, wait for the specified delayTime
  // }

  TickType_t startTick = xTaskGetTickCount();
  TickType_t waitTicks = pdMS_TO_TICKS(delayTime);  // 1000 ms wait

  while (xTaskGetTickCount() - startTick < waitTicks) {
    // Optionally do something else or just spin
  }
}

void post_to_firebase(String data, String path) {
  // default argument of waitResponse(String expected_answer = "OK", unsigned int timeout = 2000)
  // Serial1.flush();  //clear buffer
  Serial1.println("AT+HTTPTERM");
  waitResponse();
  delay_ms(DELAY_MS);

  // Serial1.flush();  //clear buffer
  Serial1.println("AT+HTTPINIT");
  waitResponse();
  delay_ms(DELAY_MS);

  // Serial1.flush();  //clear buffer

  Serial1.println("AT+HTTPPARA=\"URL\"," + path + ".json?auth=" + FIREBASE_SECRET + ":443");
  // Serial1.println("AT+HTTPPARA=\"URL\"," + FIREBASE_HOST_END + ".json?auth=" + FIREBASE_SECRET + ":443");
  // Serial1.println("AT+HTTPPARA=\"URL\"," + FIREBASE_HOST + ".json?auth=" + FIREBASE_SECRET + ":443");
  waitResponse();
  delay_ms(DELAY_MS);

  // Serial1.flush();  //clear buffer
  Serial1.println("AT+HTTPPARA=\"CONTENT\",\"application/json\"");
  waitResponse();
  delay_ms(DELAY_MS);

  Serial.println(data);

  // Serial1.flush();  //clear buffer
  Serial1.println("AT+HTTPDATA=" + String(data.length()) + ",10000");
  waitResponse("DOWNLOAD");
  delay_ms(DELAY_MS);

  // Serial1.flush();  //clear buffer
  Serial1.println(data);
  waitResponse();
  delay_ms(DELAY_MS);
  //MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
  //Sending HTTP POST request
  // Serial1.flush();  //clear buffer
  Serial1.println("AT+HTTPACTION=1");
  waitResponse();
  delay_ms(DELAY_MS);

  //MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
  //+HTTPACTION: 1,603,0 (POST to Firebase failed)
  //+HTTPACTION: 0,200,0 (POST to Firebase successfull)
  // Serial1.flush();  //clear buffer
  // Serial1.println("AT+HTTPREAD=0,30");
  // if (waitResponse("name", 5000)) Serial.println("send success");
  // for (uint32_t start = millis(); millis() - start < 20000;) {
  //   String response;
  //   if (Serial1.available() > 0) {
  //     response = Serial1.readString();
  //   }

  //   if (response.indexOf("name") > 0) {
  //     Serial.println(response);
  //     Serial.println("send success");
  //     //set flag sendsuccess to true
  //     break;
  //   }
  // }
  delay_ms(DELAY_MS);

  // Serial1.flush();  //clear buffer
  Serial1.println("AT+HTTPTERM");
  waitResponse();
  delay_ms(DELAY_MS);
}

bool waitResponse(String expected_answer = "OK", unsigned int timeout = 2000)  //uncomment if syntax error (esp8266)
{
  uint8_t x = 0, answer = 0;
  String response;

  //Clean the input buffer
  // while (Serial1.available() > 0) Serial1.read();

  //NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
  // previous = millis();
  // unsigned long previous;

  TickType_t previous = xTaskGetTickCount();
  TickType_t waitTicks = pdMS_TO_TICKS(timeout);

  do {
    //if data in UART INPUT BUFFER, reads it
    if (Serial1.available() > 0) {
      char c = Serial1.read();
      response.concat(c);
      x++;
      //checks if the (response == expected_answer)
      if (response.indexOf(expected_answer) > 0) {
        answer = 1;

        // co the comment dong nay khi chay that
        Serial.println(response);
        return 1;
      }
    }
    // } while ((answer == 0) && ((millis() - previous) < timeout));
  } while ((answer == 0) && ((xTaskGetTickCount() - previous) < waitTicks));

  //NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

  return 0;
}
