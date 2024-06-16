import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import { getDatabase, ref, get, child } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-database.js";

const firebaseConfig = {
    apiKey: "AIzaSyDmCd14uqnf0Z5d6bnrm9OnWlU9OJRrJl4",
    authDomain: "datn-43437.firebaseapp.com",
    databaseURL: "https://datn-43437-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "datn-43437",
    storageBucket: "datn-43437.appspot.com",
    messagingSenderId: "529783414922",
    appId: "1:529783414922:web:d989ca2ddb7825199e8d73",
    measurementId: "G-FF9SLCD8BX"
};
const app = initializeApp(firebaseConfig);
const db = getDatabase();

var orderID; // orderOD is ex: 20139049@....
// const orderIdH1 = document.getElementById("orderIDh1");

////////////////////////////////////GET USER EMAIL NAME USING GET DATA FROM URL
document.addEventListener("DOMContentLoaded", function () {
    var urlParams = new URLSearchParams(window.location.search);
    orderID = urlParams.get("order_id");

    // orderIdH1.textContent = orderID
    console.log("Passed data: " + orderID);

    // get data from order path then create form and pass data to form
    get(ref(db, `orders/${orderID}`)).then((snapshot) => {
        if (snapshot.exists()) {
            // val contain all information of order
            // console.log(snapshot.val());
            const allValueData = snapshot.val();
            // allValueData is all key and value in the order path in firebase
            fillFormOfFirebaseData(allValueData);
        } else {
            console.log("No data available");
        }
    }).catch((error) => {
        console.error(error);
    });


});

// get form container that is fieldset
const stopsContainer = document.getElementById('formContainer');

// create list to contain location name and latlng data
var latlnglistName = [];
var addressNames = [];

function fillFormOfFirebaseData(allValueData) {
    const numsAddress = parseInt(allValueData["numsStop"]); // String
    console.log(numsAddress);

    // create div to contain data from firebase
    const allStopDiv = document.createElement('div');
    allStopDiv.setAttribute('id', "allStopDiv");

    // save location and latlng to list
    // for (let i = 1; i <= numsAddress; ++i) {
    //     addressNames.push(allValueData[`location${i}`])
    //     latlnglistName.push(allValueData[`address${i}`])
    // }

    // console.log(addressNames);
    // contain name of address
    // console.log(latlnglistName);
    // ['kinh độ: 10.850313 ,Vĩ độ: 106.771933', 'kinh độ: 10.799795 ,Vĩ độ: 106.707566']

    // create form base on each stop address
    for (let i = 0; i < numsAddress; ++i) {
        // pass name and latlng name of each stop address
        allStopDiv.appendChild(addStopInfor(i + 1, "", ""));
    }
    stopsContainer.appendChild(allStopDiv);

    // fill form
    const form = document.getElementById('form_to_send');
    for (let key in allValueData) {
        if (allValueData.hasOwnProperty(key)) {
            // Find the corresponding input field by name attribute
            //   const inputElement = form.elements[key];
            var inputElement;
            try {
                inputElement = form.elements[key];
                // Rest of your code that uses the inputElement variable
            } catch (error) {
                // console.log(error);
            }
            // error is not important, that is the key of fb is not have in form element

            if (inputElement) {
                // Set the value of the input field from JSON data
                inputElement.value = allValueData[key];
            }
        }
    }
}


function addStopInfor(index, addressName, latlnglistName) {
    const stopDiv = document.createElement('div');
    stopDiv.classList.add('eachStop');
    stopDiv.classList.add('css_eachStop');

    // header
    const stopHeading = document.createElement('h1');
    stopHeading.textContent = 'Điểm dừng ' + index;

    // row dia chi, row 1
    const rowAddLoc1 = document.createElement('div');
    rowAddLoc1.classList.add('row_form');
    // tao 2 col cua row 1
    const colAdd = createCol("address", "Địa chỉ:", "input", "text", index, 1, addressName);
    const colLoc = createCol("location", "Tọa độ:", "input", "text", index, 1, latlnglistName);
    rowAddLoc1.appendChild(colAdd);
    rowAddLoc1.appendChild(colLoc);

    // row khach hang sdt, row 2
    const rowCustomer2 = document.createElement('div');
    rowCustomer2.classList.add('row_form');
    // tao 2 col cua row 2
    const colName = createCol("name", "Họ tên:", "input", "text", index, 2,);
    const colPhone = createCol("phone", "số điện thoại:", "input", "tel", index, 2,);
    rowCustomer2.appendChild(colName);
    rowCustomer2.appendChild(colPhone);

    // row ten hang, khoi luong row 3
    // const rowCargo3 = document.createElement('div');
    // rowCargo3.classList.add('row_form');
    // // tao 2 col cua row 3
    // const colCargoName = createCol("cargo", "Tên hàng:", "input", "text", index, 3,);
    // const colTon = createCol("weight", "khối lượng (tấn):", "input", "number", index, 3,);
    // rowCargo3.appendChild(colCargoName);
    // rowCargo3.appendChild(colTon);

    // row ten hang, khoi luong row 4
    // const rowTempHum4 = document.createElement('div');
    // rowTempHum4.classList.add('row_form');
    // rowTempHum4.setAttribute('id', 'tempHumCheck' + index);
    // // tao 2 col cua row 4
    // const colTemp = createColTempHum("Temp", "Khoảng nhiệt độ:", "number", index, 4, "từ -40 đến 20 độ", -40, 10, 20);
    // const colHum = createColTempHum("Hum", "Khoảng độ ẩm:", "number", index, 4, "từ 60 đến 80 %", 60, 70, 80);
    // rowTempHum4.appendChild(colTemp);
    // rowTempHum4.appendChild(colHum);

    // row ten hang, khoi luong row 5
    const rowCargoMethodNote5 = document.createElement('div');
    rowCargoMethodNote5.classList.add('row_form');
    // tao 2 col cua row 5
    const colCargoMethod = createCol("typeCargo", "Phương thức:", "select", "", index, 5,);
    const colNote = createCol("note", "Ghi chú:", "textarea", "", index, 5,);
    rowCargoMethodNote5.appendChild(colCargoMethod);
    rowCargoMethodNote5.appendChild(colNote);

    stopDiv.appendChild(stopHeading);
    stopDiv.appendChild(rowAddLoc1);
    stopDiv.appendChild(rowCustomer2);
    // stopDiv.appendChild(rowCargo3);
    // stopDiv.appendChild(rowTempHum4);
    stopDiv.appendChild(rowCargoMethodNote5);

    return stopDiv;
}

function createCol(id, labelName, tag, inputType, index, numRow, inputValue) {
    const col50 = document.createElement('div');
    col50.classList.add('col-50');

    // label
    const label = document.createElement('label');
    label.setAttribute('for', id + index); // Thêm index vào id ex: address1
    label.textContent = labelName;

    // input
    const tagType = document.createElement(tag);
    tagType.setAttribute('id', id + index); // Thêm index vào id
    tagType.setAttribute('name', id + index); // Thêm index vào name

    if (tag == "input") {
        tagType.setAttribute('type', inputType);
    }

    if (numRow == 1) {
        tagType.readOnly = true;
        tagType.value = inputValue;
    }

    if (id == "weight") {
        tagType.min = 1;
        tagType.step = 0.1;
    }

    if (tag == "select") {
        const option1 = document.createElement('option');
        option1.setAttribute('value', 'get');
        option1.setAttribute('selected', 'true');
        option1.textContent = 'Lấy hàng';

        const option2 = document.createElement('option');
        option2.setAttribute('value', 'return');
        option2.textContent = 'Trả hàng';

        tagType.appendChild(option1);
        tagType.appendChild(option2);
    }

    if (tag == "textarea") {
        tagType.classList.add("textarea_height");
    }

    tagType.setAttribute('placeholder', 'nhập ' + labelName.toLowerCase()); // placeholder
    tagType.required = true; // required

    col50.appendChild(label);
    col50.appendChild(tagType);
    return col50;
}

function createColTempHum(id, labelName, inputType, index, numRow, spanName, min, middle, max) {
    const col50 = document.createElement('div');
    col50.classList.add('col-50');

    // label
    const label = document.createElement('label');
    label.setAttribute('for', "min" + id + index); // Thêm index vào id ex: "min" + id + index = "min" + "Temp" + index
    label.textContent = labelName;

    // span1
    const span1 = document.createElement('span');
    span1.textContent = spanName;

    // range of temp or hum
    const divTwoInput = document.createElement('div');
    divTwoInput.classList.add('twoInput');

    const input1 = document.createElement('input');
    input1.setAttribute('type', inputType);
    input1.setAttribute('id', "min" + id + index); // Thêm index vào id
    input1.setAttribute('name', "min" + id + index); // Thêm index vào name
    input1.min = min;
    input1.max = middle;

    const span2 = document.createElement('span');
    span2.textContent = "đến";

    const input2 = document.createElement('input');
    input2.setAttribute('type', inputType);
    input2.setAttribute('id', "max" + id + index); // Thêm index vào id
    input2.setAttribute('name', "max" + id + index); // Thêm index vào name
    input2.min = middle;
    input2.max = max;

    divTwoInput.appendChild(input1);
    divTwoInput.appendChild(span2);
    divTwoInput.appendChild(input2);

    col50.appendChild(label);
    col50.appendChild(span1);
    col50.appendChild(divTwoInput);

    return col50;
}
