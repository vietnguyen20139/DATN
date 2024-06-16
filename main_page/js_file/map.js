// Create a map
const key = '6uivl76ZjIngRjPV4OeW';

//const map = L.map('map', { zoomControl: false }).flyTo([10.850071, 106.771636], 20); //starting position
// the map needs an initial center and zoom level before you can perform certain operations, 
// like adding markers or fitting bounds. Make sure you set a default view when you initialize the map, 
// like this:
const map = L.map('map', { zoomControl: false, maxZoom: 18 }).setView([10.850071, 106.771636], 20);

//add zoom control with your options
L.control.zoom({
    position: 'bottomright'
}).addTo(map);

L.tileLayer(`https://api.maptiler.com/maps/streets-v2/{z}/{x}/{y}.png?key=${key}`, { //style URL
    // L.tileLayer(`https://api.maptiler.com/maps/openstreetmap/{z}/{x}/{y}.jpg?key=6uivl76ZjIngRjPV4OeW`, { //style URL
    tileSize: 512,
    zoomOffset: -1,
    minZoom: 1,
    attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>',
    crossOrigin: true
}).addTo(map);

// Routing
// Create an empty routing control
const router_line = L.Routing.control({
    // waypoints: waypoints_first,
    // null waypoint and the set waypoint
    waypoints: [null],
    routeWhileDragging: false,
    showAlternatives: true,
    draggableWaypoints: false, // user can not drag on marker
    addWaypoints: false, // when user click on routing, it not add new marker
    show: false, // hide the itinerary panel on the right side of the map 
    createMarker: function () {
        return null; // Return null to disable marker creation
    }
}).addTo(map);

// Adding a Scale Bar in Leaflet
L.control.scale({
    metric: true,
    imperial: true,
    maxWidth: 100,
    position: 'bottomright'
}).addTo(map);

// Create an array of LatLng points
var latlngs_polyline_black; // use in onValue(router_location_path, (snapshot) => {


// create marker for auto
var car_marker;

// flag_ to ensure first time data of onchildadded is not process, first time we use data of onvalue to read once
var flag_ = false;

let number_loc_id = 0;

// Create custom icon
var blue_icon = L.icon({
    iconUrl: '../icon/blue.png',
    iconSize: [36, 36], // size of the icon
    iconAnchor: [18, 36], // Anchor point of the custom icon
    popupAnchor: [0, -36] // point from which the popup should open relative to the iconAnchor
});

var red_icon = L.icon({
    iconUrl: '../icon/red.png',
    iconSize: [72, 72], // size of the icon
    iconAnchor: [36, 72], // Anchor point of the custom icon
    popupAnchor: [0, -72] // point from which the popup should open relative to the iconAnchor
});

var yellow_icon = L.icon({
    iconUrl: '../icon/yellow.png',
    iconSize: [36, 36], // size of the icon
    iconAnchor: [18, 36], // Anchor point of the custom icon
    popupAnchor: [0, -36] // point from which the popup should open relative to the iconAnchor
});

var car_icon = L.icon({
    iconUrl: '../icon/truck.png',
    iconSize: [48, 48], // size of the icon
    iconAnchor: [24, 40], // Anchor point of the custom icon
    popupAnchor: [0, -36] // point from which the popup should open relative to the iconAnchor
});

// Create circle options
// canh bao ca hum, temp
var red_circle_op = {
    color: 'red',
    fillColor: '#ff6262',
    fillOpacity: 0.5,
    radius: 500
}

// mo cua
var blue_circle_op = {
    color: 'blue',
    fillColor: '#3b3bff',
    fillOpacity: 0.5,
    radius: 500
}

// vung dich den
var green_circle_op = {
    color: 'green',
    fillColor: '#0aff0a',
    fillOpacity: 0.5,
    radius: 500
}

// canh bao 1 trong 2 hum, temp
var yellow_circle_op = {
    color: 'yellow',
    fillColor: '#ffff4e',
    fillOpacity: 0.5,
    radius: 500
}

// diem tren dot-line
var black_circle_op = {
    color: 'black',
    // fillColor: '#0aff0a',
    fillOpacity: 0.5,
    radius: 20
}

// FIREBASE
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import { getDatabase, ref, onValue, onChildAdded, query, limitToLast, get, orderByChild, orderByValue, orderByKey } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-database.js";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
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

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getDatabase();

////////////////////////////////////GET USER EMAIL NAME USING GET DATA FROM URL
var orderID;
var h3OrderText = document.getElementById("order_id");
var CargoName = document.getElementById("cargo1");
var driverName = document.getElementById("driver");
// var driverPhone = document.getElementById("driver_phone");
var carName = document.getElementById("car_name");

// use to containe current location information to show in list
var currentLocationName;
var currentGeoName;
var geo_loc = document.getElementById("geo_loc");
var name_loc = document.getElementById("name_loc");

var temp_loc = document.getElementById("temp_text");
var hum_loc = document.getElementById("hum_text");
var speed_loc = document.getElementById("speed_text");

// get div of div containe current_loc
var currentDivLoc = document.getElementById("current_loc");

let arrNameOfStopAddress = [];
let arrGeoOfStopAddress = [];

document.addEventListener("DOMContentLoaded", function () {
    var urlParams = new URLSearchParams(window.location.search);

    // set information for order
    orderID = urlParams.get("order_id");

    h3OrderText.textContent = orderID
    console.log("Passed data: " + orderID);


    // get id of the li contain current location infor

    // currentDivLoc.addEventListener("click", function () {
    //     console.log("latlngName");
    //     // map.flyTo(new_location);/
    // })
    // then call the map and get data firebase when get orderID successly
    beginMap();
});

function setOrderInfor(cargofb, driverfb, driverPhonefb, carNamefb) {
    CargoName.textContent = cargofb;
    driverName.textContent = driverfb;
    // driverPhone.textContent = driverPhonefb;
    carName.textContent = carNamefb;
}

function createStopAddressInforLi(index, address_name, latlngName, typeCargo, note) {
    // Get the parent <ul> element
    const ulElement = document.querySelector(".sortable_list");

    // Create the new <li> element
    const newLiElement = document.createElement("li");
    newLiElement.classList.add("item");

    // Create the inner <div> element
    const divElement1 = document.createElement("div");
    divElement1.classList.add("information_field");
    divElement1.classList.add("hover_location_field");
    divElement1.setAttribute("id", `stop${index}`);

    // Create the <h4> element
    const h4Element = document.createElement("h4");
    h4Element.textContent = "Điểm dừng " + index;
    h4Element.classList.add("inline_display");


    // Create the <p> element with speed text
    const pElement_address = document.createElement("p");
    pElement_address.classList.add("inline_display");
    pElement_address.setAttribute("id", `name_loc${index}`);
    pElement_address.textContent = address_name;

    // Create the <p> element with speed text
    const pElement_latlng = document.createElement("p");
    pElement_latlng.classList.add("inline_display");
    pElement_latlng.setAttribute("id", `latlng_loc${index}`);
    pElement_latlng.textContent = latlngName;

    // Append the <h4> and <p> elements to the inner <div>
    divElement1.appendChild(h4Element);
    divElement1.appendChild(document.createElement("br"));
    divElement1.appendChild(pElement_address);
    divElement1.appendChild(document.createElement("br"));
    divElement1.appendChild(pElement_latlng);
    // divElement.appendChild(document.createElement("br"));
    // divElement.appendChild(pElement);

    // Create the inner <div> 2 element
    const divElement2 = document.createElement("div");
    divElement2.classList.add("information_field");

    const h4Element2 = document.createElement("h4");
    h4Element2.textContent = (typeCargo == "get") ? "Lấy hàng" : "Trả hàng";
    h4Element2.classList.add("inline_display");

    const h4Element3 = document.createElement("h4");
    h4Element3.textContent = "Ghi chú: "
    h4Element3.classList.add("inline_display");
    // Create the <p> element with speed text
    const pElement_note = document.createElement("p");
    pElement_note.classList.add("inline_display");
    pElement_note.setAttribute("id", `note${index}`);
    pElement_note.textContent = note;

    divElement2.appendChild(h4Element2);
    divElement2.appendChild(document.createElement("br"));
    divElement2.appendChild(h4Element3);
    divElement2.appendChild(pElement_note);
    // divElement1.appendChild(document.createElement("br"));


    // Append the inner <div> to the <li> element
    newLiElement.appendChild(divElement1);
    newLiElement.appendChild(divElement2);

    // Append the new <li> element to the parent <ul>
    ulElement.appendChild(newLiElement);

    // set click event to div contain locaion
    const regex = /[-+]?[0-9]*\.?[0-9]+/g;
    const numbers = latlngName.match(regex);

    const latitude = parseFloat(numbers[0]);
    const longitude = parseFloat(numbers[1]);
    const latlngCurrentDiv1 = L.latLng(latitude, longitude);
    divElement1.addEventListener("click", function () {
        console.log(latlngName);
        map.flyTo(latlngCurrentDiv1, 18);
    })
}

// undefine orderid, because the document is not load
// console.log(`/orders/${orderID}`);

function beginMap() {

    // document is loaded
    console.log(`/orders/${orderID}`);
    // Create a reference to path contain location to draw route in "test/endBegin"
    // const router_location_path = ref(database, 'test/endBegin');
    const router_location_path = ref(database, `/orders/${orderID}`);
    // const router_location_path = ref(database, '/orders/201390490');

    // create waypoints to contain location to draw router
    let waypoints_first = [];

    let location_line = [];
    // add dot-line
    latlngs_polyline_black = L.polyline(location_line, {
        color: 'black',
        dashArray: '5, 5'     // Customize dash pattern (5px dash, 5px gap)
    }).addTo(map);
    // Listen for changes at the "/orders/201390490" reference and add router for first time map opens
    // onValue(router_location_path, (snapshot) => {
    //     const allValueData = snapshot.val();
    //     const numsAddress = parseInt(allValueData["numsStop"]); // String
    //     console.log(numsAddress);

    //     const regex = /[-+]?[0-9]*\.?[0-9]+/g;

    //     for (let i = 1; i <= numsAddress; i++) {
    //         var latlngName = allValueData[`location${i}`]; //"Kinh độ: 10.850313, Vĩ độ: 106.771933"
    //         // console.log(latlngName)
    //         const numbers = latlngName.match(regex);

    //         const latitude = parseFloat(numbers[0]);
    //         const longitude = parseFloat(numbers[1]);

    //         const latlng = L.latLng(latitude, longitude);
    //         waypoints_first.push(latlng);
    //         // console.log(latitude); // Output: 10.850313
    //         // console.log(longitude); // Output: 106.771933 
    //         L.circle(latlng, green_circle_op).addTo(map);
    //         L.marker(latlng, { icon: red_icon }).addTo(map).bindPopup(latlngName);
    //     }
    //     // router_line.setWaypoints(waypoints_first);  
    //     console.log("in ovalue" + waypoints_first)
    // });

    get(router_location_path).then((snapshot) => {
        if (snapshot.exists()) {
            const allValueData = snapshot.val();
            const numsAddress = parseInt(allValueData["numsStop"]); // String

            // get other data carName, driver, cargo1
            const cargofb = allValueData["cargo1"];
            const driverfb = allValueData["driver"];
            const driverPhonefb = allValueData["driverPhone"];
            const carNamefb = allValueData["car"];

            setOrderInfor(cargofb, driverfb, driverPhonefb, carNamefb);
            console.log(numsAddress);

            const regex = /[-+]?[0-9]*\.?[0-9]+/g;

            for (let i = 1; i <= numsAddress; i++) {
                var latlngName = allValueData[`location${i}`]; //"Kinh độ: 10.850313, Vĩ độ: 106.771933"
                // console.log(latlngName)

                // get 10.850313 and 106.771933 from Kinh độ: 10.850313, Vĩ độ: 106.771933
                const numbers = latlngName.match(regex);

                const latitude = parseFloat(numbers[0]);
                const longitude = parseFloat(numbers[1]);

                const latlng = L.latLng(latitude, longitude);
                waypoints_first.push(latlng);
                // console.log(latitude); // Output: 10.850313
                // console.log(longitude); // Output: 106.771933 
                L.circle(latlng, green_circle_op).addTo(map);
                L.marker(latlng, { icon: red_icon }).addTo(map).bindPopup(latlngName);

                // get adress name and geo name
                const address_name = allValueData[`address${i}`];

                // get type of cargo: lay hang or tra hang
                const typeCargo = allValueData[`typeCargo${i}`];
                const note = allValueData[`note${i}`];

                // arrNameOfStopAddress.push(address_name);
                // arrGeoOfStopAddress.push(latlngName);

                createStopAddressInforLi(i, address_name, latlngName, typeCargo, note);
                // console("i is" + i)
            }
            // console.log(arrGeoOfStopAddress);
            // console.log(arrNameOfStopAddress);
            // get 1 time data and set waypoint
            router_line.setWaypoints(waypoints_first);
            console.log("in ovalue" + waypoints_first)
        } else {
            console.log("No data available");
        }
    }).catch((error) => {
        console.error(error);
    });

    // read one time "test/new" reference once to draw dot-line for old location
    // const new_latLng_path = query(ref(database, "test/new3"), orderByChild("data"));
    const new_latLng_path = query(ref(database, `/orders/${orderID}/datas`), orderByChild("data"));
    // const new_latLng_path = query(ref(database, "/orders/201390490/datas"), orderByChild("data"));

    // onValue(new_latLng_path, (snapshot) => {
    //     console.log("read once time");
    //     let location_line = [];
    //     // console.log(snapshot.val());
    //     if (snapshot.val() != 0) {
    //         // console.log(snapshot.key); // key is new3
    //         snapshot.forEach((childSnapshot) => {
    //             // const key = childSnapshot.key; // key is jbNw-qWOChL-AJpWh17Xl
    //             const value = childSnapshot.val(); // value is {data: 0,11,...} => value.data is 0,11,21.221,...
    //             const value_data = value.data; // String

    //             // console.log(typeof(value_data));
    //             // console.log(value_data);

    //             const value_data_split = value_data.split(","); // ["4", "78", "10.844243", "106.782023", "60", "30"]

    //             // Store the values in a new array
    //             const arr_number = value_data_split.map((value) => parseFloat(value)); // [4, 78, 10.844243, 106.782023, 60, 30]

    //             const old_location = L.latLng(arr_number[2], arr_number[3]);
    //             location_line.push(old_location);
    //         });

    //         for (let i = 0; i < location_line.length - 1; i++) {
    //             // console.log(location_line[i]); // {lat: ..., lng: ...}
    //             // console.log("i is", i);
    //             // var old_marker = L.marker(location_line[i]).addTo(map).setIcon(yellow_icon);
    //             // old_marker.bindPopup('dia chi so ' + i.toString());
    //             var old_circle = L.circle(location_line[i], black_circle_op).addTo(map);
    //             old_circle.bindPopup('dia chi so ' + i.toString());
    //         }

    //         car_marker = L.marker(location_line[location_line.length - 1]).addTo(map).setIcon(car_icon);
    //         // add dot-line
    //         latlngs_polyline_black = L.polyline(location_line, {
    //             color: 'black',
    //             dashArray: '5, 5'     // Customize dash pattern (5px dash, 5px gap)
    //         }).addTo(map);
    //         // Zoom the map to fit the bounds of the polyline
    //         map.fitBounds(latlngs_polyline_black.getBounds()); //latlns_polyline must not null

    //         number_loc_id = location_line.length; // use for check if new data have loc is old or new in onchildadded 
    //         // console.log(number_loc_id);
    //         flag_ = true;
    //     } else {
    //         console.log("dont have data");
    //     }
    // }, {
    //     onlyOnce: true
    // });

    // limittolast to get just last new data
    // const new_latLng_last_path = query(ref(database, "test/new3"), orderByChild("data"), limitToLast(1)); // use for limittolast
    // const new_latLng_last_path = query(ref(database, `/orders/${orderID}/datas`), orderByChild("data"), limitToLast(1));
    const new_latLng_last_path = query(ref(database, `/orders/${orderID}/datas`)); // use for limittolast
    // use for limittolast
    // const new_latLng_last_path = query(ref(database, "/orders/201390490/datas"), orderByChild("data"), limitToLast(1)); // use for limittolast

    // vvariable for onchildadded
    var max_id = 0;
    var isEndFirstTimeOnchildadded = false;

    var maxLat;
    var maxLng;
    var marker_max;
    // caculate the num child, if num_child_for_first = numbers of all child in datas then we
    // know the first time onchildadded loop all list is finish 
    var num_child_for_first = 0;
    // onchildeadded is call befrore get so we call get firsr and then call onchildadded
    var totalChildCountData = 0;
    get(new_latLng_last_path).then((snapshot) => {
        if (snapshot.exists()) {
            console.log(snapshot.key)
            // get number of child in datas to show the last data of location
            totalChildCountData = snapshot.size;

            // Use the totalChildCount as desired
            console.log("Total child count:", totalChildCountData);


        } else {
            console.log("No data available");
        }

        callOnchildadded();
    }).catch((error) => {
        console.error(error);
    });


    function callOnchildadded() {
        onChildAdded(new_latLng_last_path, (snapshot) => {
            // first time loop all list, and then new data is add then get just new data
            // if (flag_) {

            num_child_for_first++;
            // console.log(num_child_for_first)
            // console.log(totalChildCountData)



            // console.log("flag is true, loc id is: ", number_loc_id);
            // console.log("read last new data");
            // console.log(snapshot.val()); // value is {data: 0,11,...} => value.data is 0,11,21.221,...

            const new_value = snapshot.val(); // value is {data: 0,11,...} => value.data is 0,11,21.221,...
            const new_value_data = new_value.data; // String
            const new_value_data_split = new_value_data.split(","); // ["4", "78", "10.844243", "106.782023", "60", "30"]
            // Store the values in a new array
            const arr_number = new_value_data_split.map((value) => parseFloat(value)); // [4, 78, 10.844243, 106.782023, 60, 30]
            const new_location = L.latLng(arr_number[2], arr_number[3]);
            const temp = arr_number[4];
            const hum = arr_number[5];
            const speed = arr_number[1];

            console.log("ID is: " + arr_number[0] + "............");

            location_line.push(new_location);
            // // add dot-line
            // latlngs_polyline_black = L.polyline(location_line, {
            //     color: 'black',
            //     dashArray: '5, 5'     // Customize dash pattern (5px dash, 5px gap)
            // }).addTo(map);

            // To update an existing polyline with new locations, you can use the .setLatLngs() method 
            // on the existing polyline object instead of creating a new one. 
            latlngs_polyline_black.setLatLngs(location_line).addTo(map);

            // Zoom the map to fit the bounds of the polyline
            // map.fitBounds(latlngs_polyline_black.getBounds()); //latlns_polyline must not null

            // Create a marker with the LatLng new_location and add it to the map
            // const marker = L.marker(new_location).addTo(map);
            const marker = L.marker(new_location, { icon: blue_icon }).addTo(map).bindPopup(arr_number[0] + " ,Tọa độ: " + arr_number[2] + "," + arr_number[3]);
            // L.marker(latlng, { icon: red_icon }).addTo(map).bindPopup(latlngName);

            // check if new data is last data
            if (arr_number[0] > max_id) {
                // dia chi co so id lon nhat la toa do moi nhat
                max_id = arr_number[0];
                //change route from last new data to waypoints
                // add new element to first of arr
                maxLat = arr_number[2];
                maxLng = arr_number[3];
                var maxLocation = L.latLng(maxLat, maxLng);
                marker_max = L.marker(maxLocation, { icon: blue_icon }).addTo(map).bindPopup(max_id + " ,Tọa độ: " + maxLat + "," + maxLng);

                // update first time when onchildadded finish loop each data in snapshot first time open map
                // passCurrentNameAndGeoLocToList(arr_number[2], arr_number[3]);
                console.log("max id is " + arr_number[0]);
                console.log(maxLat + "," + maxLng);

                // if first time call onchildadded end, then each time new child is add, the 
                if (isEndFirstTimeOnchildadded) {
                    console.log("new child added call this when first time call onchildadded end");
                    passCurrentNameAndGeoLocToList(arr_number[2], arr_number[3]);
                    // update each time when onchildadded have new data in snapshot
                    // updateLocation(new_location);

                    setTempHumSpeed(temp, hum, speed);
                    // map.panTo(new L.latLng(maxLat, maxLng), 18);
                    // map.flyTo(L.latLng(maxLat, maxLng), 18);
                    // map.setView(L.latLng(maxLat, maxLng), 18);

                    marker_max.openPopup();

                    currentDivLoc.removeEventListener("click", currentDivLocEventClick);

                    // set zoom when click on div contain current address infor
                    currentDivLoc.addEventListener("click", function () {
                        currentDivLocEventClick(marker_max, maxLat, maxLng);
                    })
                }

                //map.panTo(new L.latLng(maxLat, maxLng));
            }

            // when num_child_for_first == totalChildCountData it means that first time call onchildadded end, then
            // we call passCurrentNameAndGeoLocToList to set location name first for last address in firebase when first time open map
            // and call updatdelocation to set last location
            if (num_child_for_first == totalChildCountData) {
                console.log(num_child_for_first + ": " + totalChildCountData)
                console.log("end first time");
                // set name of location to current location when first time call onchildadded end
                passCurrentNameAndGeoLocToList(arr_number[2], arr_number[3]);
                isEndFirstTimeOnchildadded = true;
                // updateLocation(new_location);

                // add the last item to waypoints_first, so next time we just delete the first waypoint 
                // and the list on stop address is not delete
                // waypoints_first.unshift(new_location);
                // router_line.setWaypoints(waypoints_first);
                // map.flyTo(new_location, 14);

                setTempHumSpeed(temp, hum, speed);
                map.flyTo(L.latLng(maxLat, maxLng), 18);
                marker_max.openPopup();

                currentDivLoc.removeEventListener("click", currentDivLocEventClick);

                // set zoom when click on div contain current address infor
                currentDivLoc.addEventListener("click", function () {
                    currentDivLocEventClick(marker_max, maxLat, maxLng);
                })
            }

            // console.log("max id is" + max_id);

            // router_line.setWaypoints([null]);
            // console.log("in child" + waypoints_first);
            // console.log(arr_number[0] + "toa do" + arr_number[2]+ arr_number[3])

            // console.log(waypoints_first);
            // set view to new data
            // }
        });


        function currentDivLocEventClick(marker, maxLat, maxLng) {
            console.log("click current loc div");
            // console.log("first time: max lat, max lng is: " + maxLat + "," + maxLng);
            map.flyTo(L.latLng(maxLat, maxLng), 18);

            // map.panTo(L.latLng(maxLat, maxLng));

            marker.openPopup();
        }
    }


    // waypoints_first is in scope of beginMap()
    // function updateLocation(new_location) {
    //     waypoints_first.shift(); // delete first element
    //     waypoints_first.unshift(new_location);
    //     router_line.setWaypoints(waypoints_first);
    //     map.flyTo(new_location, 14);
    // }


}

// add srearch to map
L.Control.geocoder({ placeholder: 'Tìm kiếm ở đây' }).addTo(map);

function setTempHumSpeed(temp, hum, speed) {
    temp_loc.textContent = temp;
    hum_loc.textContent = hum;
    speed_loc.textContent = speed;
}

var if5s = false;

function passCurrentNameAndGeoLocToList(lat, lng) {
    currentGeoName = "Kinh độ: " + lat + ", vĩ độ: " + lng;
    // reset name location
    geo_loc.textContent = "";

    // set text of kinh do vi do
    // L.control.options.geocoder.reverse([lat, lng]).run( function (results) {
    //     var r = results[0];
    //     var name_loc;
    //     // get lat and lng 
    //     var lat = e.latlng.lat.toFixed(6);
    //     var lng = e.latlng.lng.toFixed(6);
    //     if (r) {
    //         name_loc = r.name;
    //     }
    //     console.log(name_loc);
    // });

    const reverseGeocodingURL = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}`;

    // Send a GET request to the reverse geocoding URL
    // fetch is qucikly than get
    fetch(reverseGeocodingURL)
        .then(response => response.json())
        .then(data => {
            // Extract the location name from the response
            const locationName = data.display_name;

            geo_loc.textContent = currentGeoName;

            // Convert Pham Van Dong Boulevard, Linh Trung Ward, Thủ Đức, 
            // Ho Chi Minh City, 71221, Vietnam
            // to Pham Van Dong Boulevard, Linh Trung Ward, Thủ Đức, 
            // Ho Chi Minh City
            if (data) {
                // const lastCommaIndex = locationName.lastIndexOf(',');
                // const secondLastCommaIndex = locationName.lastIndexOf(',', lastCommaIndex - 1);
                // Remove the portion after the last comma
                // const cleanedString = locationName.substring(0, secondLastCommaIndex);

                // name_loc.textContent = cleanedString;
                // Use the location name as desired
                // console.log(locationName);
                // console.log(cleanedString);

                name_loc.textContent = locationName;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });



    // $.get(`https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${lat}4&lon=${lng}`, function (data) {
    //     // Use data.address to get the address components (e.g., city, street, etc.)
    //     // console.log(data.address)
    //     var addr = data.display_name;
    //     // console.log(addr);

    //     // Find the index of the last comma
    //     const lastCommaIndex = addr.lastIndexOf(',');

    //     // Find the index of the comma before the last comma
    //     const secondLastCommaIndex = addr.lastIndexOf(',', lastCommaIndex - 1);
    //     // Remove the portion after the last comma
    //     const cleanedString = addr.substring(0, secondLastCommaIndex);

    //     console.log(cleanedString);
    //     currentLocationName = cleanedString;
    //     name_loc.textContent = currentLocationName;

    // });

    // if (if5s) {
    //     setInforCurrentLocatonAfter5s();
    // }
}

// // set the name and current address of current location after 5s
// setTimeout(function () {
//     // Your custom function to be executed after 7 seconds
//     console.log('Map has loaded after 5 seconds!');
//     geo_loc.textContent = currentGeoName;
//     name_loc.textContent = currentLocationName;
//     if5s = true;
//     // Call any other functions or perform additional actions here
// }, 5000);

// function setInforCurrentLocatonAfter5s() {
//     console.log('call setInforCurrentLocatonAfter5s');

//     geo_loc.textContent = currentGeoName;
//     name_loc.textContent = currentLocationName;
// }
function googleTranslateElementInit() {
    new google.translate.TranslateElement({ pageLanguage: 'en', includedLanguages: 'vi', layout: google.translate.TranslateElement.InlineLayout.SIMPLE }, 'name_loc');
}

////////////////////////////////// EXAMPLE ///////////////////////////////////

// how to add, delete a location of waypoints. How to add waypoints to route
// let waypoints_first = [
//     L.latLng(10.853480, 106.751473),
//     L.latLng(10.845639, 106.795460)
// ];

// -----------add new location ---------------------
// waypoints_first.push(L.latLng(10.844563, 106.775757));
// console.log(waypoints_first);

// -----------delete first location of waypoints ---------------------
// waypoints_first.shift();

// -----------set waypoint to rou_line so the line is draw on map ---------------------
// router_line.setWaypoints(waypoints_first);

// -----------add new marker and popup when click--------------------
// const marker_test = L.marker([10.844499, 106.770696]).addTo(map);
// marker_test.bindPopup("popupContent"); // click is open
// .openPopup(); // to open

// marker_test.on('mouseover', function (event) {
//     marker_test.bindPopup('<p>Hello world!<br />This is a nice popup.</p>').openPopup();
// });
// marker_test.on('mouseout', function (event) {
//     marker_test.closePopup();
// });

// var popup = L.popup(L.latLng(10.844499, 106.770696), {content: '<p>Hello world!<br />This is a nice popup.</p>'})
//     // .openOn(map);

// -------------add custom marker and circle------------------------
// L.marker([10.858186, 106.748943], {icon: red_icon}).addTo(map).bindPopup("ok");
// L.circle([10.858186, 106.748943], yellow_circle_op).addTo(map);

// ----------------add dot-line---------------------
// latlngs_polyline_red = L.polyline(waypoints_first, {
//     color: 'black',
//     dashArray: '5, 5'     // Customize dash pattern (5px dash, 5px gap)
// }).addTo(map);
// // Zoom the map to fit the bounds of the polyline
// map.fitBounds(latlngs_polyline_red.getBounds()); //latlns_polyline must not null
// console.log(typeof(all_value));




