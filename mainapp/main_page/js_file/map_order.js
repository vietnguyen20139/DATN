// Create a map
const key = '6uivl76ZjIngRjPV4OeW';

// const map = L.map('map', {zoomControl: false}).setView([10.850071, 106.771636], 14); //starting position

//////////////////test map click////////////////////////
const map = L.map('map', { zoomControl: false }).setView([10.850071, 106.771636], 30),
    selector = L.DomUtil.get('geocode-selector'),
    control = new L.Control.Geocoder({ geocoder: null });


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
    show: true, // hide the itinerary panel on the right side of the map 
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

// create waypoints to contain location to draw router
let waypoints_first = [];

// Create an array of LatLng points
var latlngs_polyline_black; // use in onValue(router_location_path, (snapshot) => {

// create marker for auto
var car_marker;

// flag_ to ensure first time data of onchildadded is not process, first time we use data of onvalue to read once
var flag_ = false;

var red_icon = L.icon({
    iconUrl: '../icon/red.png',
    iconSize: [36, 36], // size of the icon
    iconAnchor: [18, 36], // Anchor point of the custom icon
    popupAnchor: [0, -36] // point from which the popup should open relative to the iconAnchor
});


///////////////////////////FINDING LOCATION
L.Control.geocoder().addTo(map);


//////////////////////////////////CLICK ON MAP AND GET LOCATION///////////////////////////////

var marker_x;

/////////////////////////////////////////////////TEST???????????????????????????????????????????????

// Create a popup for the marker
// var popupContent_remove = '<button id="removeBtn">Remove Marker</button>';
// marker_r.bindPopup(popupContent_remove);
var marker_r = L.marker([0, 0], { icon: red_icon });
// Event handling for the popup button
marker_r.on('popupopen', function () {
    var removeBtn = document.getElementById('removeBtn');
    removeBtn.addEventListener('click', removeMarker);
});

///////////////////////////FOR LIST/////////////////////////
const sortableList = document.querySelector(".sortable_list");
const items = sortableList.querySelectorAll(".item");

//////////////////DOM//////////////////////////////
function button(label, container) {
    var btn = L.DomUtil.create('button', '', container);
    btn.setAttribute('type', 'button');
    btn.innerHTML = label;
    return btn;
}

function locationContainer(text, container) {
    var infor = L.DomUtil.create('div', '', container);
    infor.innerHTML = text;
    return infor;
}

var marker_list = [];
var marker_nums = 0;

// Define a function to handle marker removal
function removeMarker(marker_id) {
    // when click remove btn in marker then find the li item corespond to marker and remove it
    marker_list.forEach(function (marker, index) {
        // console.log(marker._id, "marker_id is: ", marker_id);
        if (marker._id == marker_id) {
            map.removeLayer(marker);
            marker_list.splice(index, 1);
            // console.log("xoa marker tai vi tri: ", index);
            // console.log("maker con lai: ",marker_list.length);

            const listItem = document.querySelector(`#li${marker_id}`);
            if (listItem) {
                listItem.remove();
            }
        }
    })
}

function removeMarkerByLi(marker_id) {
    marker_list.forEach(function (marker, index) {
        // console.log(marker._id, "marker_id is: ", marker_id);
        if (marker._id == marker_id) {
            map.removeLayer(marker);
            marker_list.splice(index, 1);
            // console.log("xoa marker tai vi tri: ", index);
            // console.log("maker con lai: ",marker_list.length);
        }
    })
}

/////////////////////phai zoom vao sau moi duoc neu khong thi ERROR/////////////////
map.on('click', function (e) {
    var locContent = "";

    // convert location to address name
    control.options.geocoder.reverse(e.latlng, map.options.crs.scale(map.getZoom()), function (results) {
        var r = results[0];
        var name_loc;
        // get lat and lng 
        var lat = e.latlng.lat.toFixed(6);
        var lng = e.latlng.lng.toFixed(6);
        if (r) {
            locContent = "<b>Địa chỉ:</b> " + r.name + "<br><b>Kinh độ:</b> " + lat + "<br><b>Vĩ độ:</b> " + lng + "<br>";
            name_loc = r.name;
        }
        // console.log(locContent);

        var container = L.DomUtil.create('div'),
            text = locationContainer(locContent, container),
            addBtn = button('Add this location', container);

        L.DomEvent.on(addBtn, 'click', function () {
            marker_nums++;
            console.log(marker_nums);

            // console.log(name_loc);
            // ` is diffrent from ', single quotes: ' and backticks: ` 

            var popupContent_remove = locContent + `<button class="removeBtn" id="${marker_nums}">Xóa địa chỉ</button>`;

            console.log(popupContent_remove);
            // marker_r.bindPopup(popupContent_remove);
            // marker_r.setLatLng(r.center).addTo(map);
            var marker = L.marker([0, 0], { icon: red_icon }).setLatLng(r.center).bindPopup(popupContent_remove).addTo(map);

            // set id marker to marker_nums so we can remove base on id
            marker._id = marker_nums;
            console.log(marker._id);

            //////////////////add name of location to list and the id of marker then when we remove the marker, the li iten
            // in list is remove
            add_to_list(name_loc, marker_nums, lat, lng);

            // add properti when marker popup content to marker
            // get marker id
            marker.on('popupopen', function (e) {
                //get marker id
                const markerId = e.target._id;

                //get btn base on marker id
                const removeBtn = document.getElementById(markerId);

                console.log("markerId: ", markerId);
                console.log(removeBtn);
                removeBtn.addEventListener('click', function () { removeMarker(markerId) });
            });

            // add marker to list so we can remove it base on marker id
            marker_list.push(marker);

            map.closePopup();
        });

        L.popup()
            .setContent(container)
            .setLatLng(e.latlng)
            .openOn(map);
    })

});

// drag and drop
const initSortableList = (e) => {
    e.preventDefault();
    const draggingItem = document.querySelector(".dragging");
    // Getting all items except currently dragging and making array of them
    let siblings = [...sortableList.querySelectorAll(".item:not(.dragging)")];

    // Finding the sibling after which the dragging item should be placed
    let nextSibling = siblings.find(sibling => {
        return e.clientY <= sibling.offsetTop + sibling.offsetHeight / 2;
    });

    // Inserting the dragging item before the found sibling
    sortableList.insertBefore(draggingItem, nextSibling);
}

sortableList.addEventListener("dragover", initSortableList);
sortableList.addEventListener("dragenter", e => e.preventDefault());

function printList() {
    const sortedItems = sortableList.querySelectorAll(".item");
    const itemOrder = Array.from(sortedItems).map(item => item.querySelector("span").textContent);
    console.log("Sorted List:", itemOrder);
}

function add_to_list(name, marker_id, lat, lng) {
    const sortableList = document.querySelector(".sortable_list");

    // Create a new list item
    const newItem = document.createElement("li");
    newItem.classList.add("item");
    newItem.draggable = true;

    // Set ID
    newItem.setAttribute("id", `li${marker_id}`);
    // store lat lng data to atttribute of li item in list
    newItem.setAttribute("d_lat", lat);
    newItem.setAttribute("d_lng", lng);
    newItem.setAttribute("nameLoc", name);

    // Create the inner structure of the new list item
    const itemDetails = document.createElement("div");
    itemDetails.classList.add("details");

    // const itemImage = document.createElement("img");
    // itemImage.src = "images/img-6.jpg";

    const itemText = document.createElement("span");
    itemText.textContent = name;

    ///////////add text to contain address but dont show, use this to make route
    // const itemText2 = document.createElement("text");
    // itemText.textContent = name;

    // itemDetails.appendChild(itemImage);
    itemDetails.appendChild(itemText);

    const dragHandle = document.createElement("i");
    dragHandle.classList.add("uil", "uil-draggabledots");

    ///////////////////////remove btn////////////////////////
    const removeBtn = document.createElement("button");
    removeBtn.textContent = "Xóa";
    removeBtn.addEventListener("click", () => {
        newItem.remove();
        removeMarkerByLi(marker_id);
        printList();
    });

    newItem.appendChild(removeBtn);
    newItem.appendChild(itemDetails);
    newItem.appendChild(dragHandle);

    // Append the new list item to the sortable list
    sortableList.appendChild(newItem);

    newItem.addEventListener("dragstart", () => {
        // Adding dragging class to item after a delay
        setTimeout(() => newItem.classList.add("dragging"), 0);
    });
    // Removing dragging class from item on dragend event
    newItem.addEventListener("dragend", () => {
        newItem.classList.remove("dragging");
        printList();
    });
};

// get lat lng address from list
function getAllItemCoordinates() {
    const listItems = document.querySelectorAll(".sortable_list li");
    const coordinates = [];

    listItems.forEach((item) => {
        const lat = item.getAttribute("d_lat");
        const lng = item.getAttribute("d_lng");

        if (lat && lng) {
            coordinates.push(L.latLng(parseFloat(lat), parseFloat(lng)));
        }
    });

    return coordinates;
}

// get name address from list
function getAllAdressNames() {
    const listItems = document.querySelectorAll(".sortable_list li");
    const addressName = [];

    listItems.forEach((item) => {
        const name = item.getAttribute("nameLoc");

        if (name) {
            addressName.push(name);
        }
    });

    return addressName;
}
//////////for find way

var button_findway = document.getElementById("findway");
var distance;
var time;
// Add event listener to the button
button_findway.addEventListener("click", function () {
    // Call getAllItemCoordinates to retrieve the coordinates
    var coordinates = getAllItemCoordinates();

    // Print the list of coordinates
    console.log(coordinates);

    ///////////////////////////////////////LAM FORM XONG ROI LAM CAI NAY
    // chia ra tung quang duong doi voi 2 diem va chon quang duong bang ngan nhat dua tren  routes.length
    // neu  routes.length = 2 thif  routes[0] la quang duong 1 va  routes.length[1] la quang duong 2
    // var distance = routes[0].summary.totalDistance;  
    // if have more than 2 location, example 3, it will find the small distance between 3 location
    // Draw waypoint
    router_line.setWaypoints(coordinates).on('routesfound', function (e) {
        var routes = e.routes;
        // alert('Found ' + routes.length + ' route(s).');
        distance = (routes[0].summary.totalDistance / 1000).toFixed(2); //km
        time = Math.floor(routes[0].summary.totalTime / 60); // minute
        // time = routes[0].summary.totalTime/3600; // second

        time = Math.ceil(time / 60); // convert to hours
        if (time < 1) {
            time = 1; // set minimum value to 1 day
        }
        console.log('routing2 ' + distance + "time: " + time);
    });

});

/////////////////////////////////////////////////  ADD NEW FORM WHEN CLICK XAC NHAN
const submitButtonStep2 = document.getElementById('submitStep2');
const clearSubmitButtonStep2 = document.getElementById('clearSubmitStep2');

const divSubmitButtonStep2 = document.getElementById('divSubmitStep2');
const divClearSubmitButtonStep2 = document.getElementById('divClearSubmitStep2');
const numsStopInput = document.getElementById("numsStop");

// const orderID = document.getElementById('orderID');

// get form container
const stopsContainer = document.getElementById('formContainer');

// get variable from other file
// When you use the import statement in JavaScript to import a module, 
// the imported module is executed or evaluated to provide the exported values. 
// If you import a module using import { user_email } from './sign_out_state.js', 
// the sign_out_state.js file will be executed to resolve the exported user_email value.

// import { user_email } from './sign_out_state.js'

var user_email; // user_email is ex: 20139049@....
////////////////////////////////////GET USER EMAIL NAME USING GET DATA FROM URL
document.addEventListener("DOMContentLoaded", function () {
    var urlParams = new URLSearchParams(window.location.search);
    user_email = urlParams.get("email");

    isOpenContainerInput.value = 1;
    console.log(isOpenContainerInput.value)

    console.log("Passed data: " + user_email);
});

submitButtonStep2.addEventListener('click', function () {
    console.log(user_email);

    setOrderIdToHeader();
    // get user order infor like total order and id_num to create orderID
    getUserOrderInfor(user_email);
    // then 
    addNumStop();
});

clearSubmitButtonStep2.addEventListener('click', function () {
    divClearSubmitButtonStep2.style.display = 'none';
    divSubmitButtonStep2.style.display = 'flex';
    const currentAllStopDivs = document.getElementById('allStopDiv');
    if (currentAllStopDivs) {
        currentAllStopDivs.remove();
    }
});

// list to contain addressname and addresslocation
var latlnglist = [];
var addressNames = [];
/////////////////
var idNumOrder;
var totalOrder;
var waitOrder;
var idNumOrderForm;

function setOrderIdToHeader() {
    const distanceRunning = document.getElementById("distanceRunning");
    const timeRunning = document.getElementById("timeRunning");

    if (!distance) {
        alert("hay tim duong o buoc 2");
        return;
    }
    console
    distanceRunning.value = distance;
    timeRunning.value = time;
}

function addNumStop() {
    addressNames = getAllAdressNames();
    latlnglist = getAllItemCoordinates();
    var numsAddress = addressNames.length;
    if (latlnglist.length <= 1) {
        // console.log("hay chon dia chi va tim duong o buoc 2");
        alert("hay chon dia chi va tim duong o buoc 2");
        return;
    }


    // hide btn submit step2 and show btn close step2
    divClearSubmitButtonStep2.style.display = 'flex';
    divSubmitButtonStep2.style.display = 'none';
    // console.log(typeof(latlnglist[0].lng)); //number

    // console.log(latlnglist[0].lat); //number

    console.log("create form");

    // set numstop 
    numsStopInput.value = latlnglist.length;
    const allStopDiv = document.createElement('div');
    allStopDiv.setAttribute('id', "allStopDiv");

    // console.log(numsAddress);
    for (let i = 0; i < numsAddress; ++i) {
        var lat = latlnglist[i].lat;
        var lng = latlnglist[i].lng;

        // console.log(lat + "in loop" + lng);
        allStopDiv.appendChild(addStopInfor(i + 1, addressNames[i], lat, lng));
    }
    stopsContainer.appendChild(allStopDiv);

}
function addStopInfor(index, addressName, lat, lng) {
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
    const colLoc = createCol("location", "Tọa độ:", "input", "text", index, 1, "kinh độ: " + lat + " ,Vĩ độ: " + lng);
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

///////////////////////////CODE FIREBASE TO GET ID
// FIREBASE
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import { getDatabase, ref, onValue, set, onChildAdded, query, limitToLast, get, orderByChild, orderByKey } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-database.js";
// import { user_email } from "./sign_out_state";

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

// // Create a reference to user/order to create id of order and get infor of total order
const db = getDatabase();
function getUserOrderInfor(user_email) {
    const email_name = user_email.split('@')[0];
    const userOrderInfor = ref(db, 'users/' + email_name + '/order');
    const userOrder = ref(db, 'users/' + email_name);

    console.log()
    onValue(userOrder, (snapshot) => { 
        console.log(snapshot)
        const user_data = snapshot.val();
        console.log(user_data)
        var phoneNumber = user_data.phone;
        var name = user_data.name;

        var createPerson = document.getElementById('createPerson');
        var phoneCreatePerson = document.getElementById('phoneCreatePerson');

        createPerson.value = phoneNumber;
        phoneCreatePerson.value = name;        
    });

    onValue(userOrderInfor, (snapshot) => {
        console.log(snapshot);
        const data = snapshot.val();
        idNumOrder = data.idnum;
        idNumOrderForm = email_name + idNumOrder;
        console.log("idNumOrderForm is " + idNumOrderForm);

        // set orderid for order
        const orderID = document.getElementById("orderID");
        orderID.value = idNumOrderForm;
    }, {
        onlyOnce: true
      });

}

////////////////////////////////////////////////////SET DATA TO FIREBASE
const formToSend = document.getElementById("form_to_send");
const submitFormBtn = document.getElementById("btnSubmitForm");
const submitFirebaseBtn = document.getElementById("submitFirebase");


var jsonFormData;
var entriesForm;

formToSend.addEventListener('submit', (e) => {
    e.preventDefault();

    const formData = new FormData(formToSend);

    entriesForm = Object.fromEntries(formData);

    // Set driver and car empty value, so app can change data
    entriesForm.driver = 0;
    entriesForm.driverPhone = 0;
    entriesForm.car = 0;
    entriesForm.status = 0;
    entriesForm.datas = 0;
    entriesForm.complete = 0;
    // console.log(res);

    // jsonFormData = JSON.stringify(res);
    // console.log(jsonFormData);

    // const entries = new Map([
    //     ['foo', 'bar'],
    //     ['baz', 42],
    //   ]);

    //   const obj = Object.fromEntries(entries);

    //   console.log(obj);
    // Expected output: Object { foo: "bar", baz: 42 }
})

submitFormBtn.addEventListener
submitFirebaseBtn.addEventListener('click', function () {
    console.log(entriesForm);
    if(entriesForm) {
    // set data in firebase
    set(ref(db, `orders/${idNumOrderForm}`), entriesForm)
        .then(() => {
            console.log("Tạo đơn thành công, dữ liệu đã được gửi lên cơ sở dữ liệu");
            alert("Tạo đơn thành công, dữ liệu đã được gửi lên cơ sở dữ liệu");

            idNumOrder++;
            setNewIdnumorderForUser(user_email, idNumOrder);
        })
        .catch((error) => {
            console.error("Error setting data in the database:", error);
            
        });
    } else {
        alert("Hãy điền tất cả các ô");
    }
})

function setNewIdnumorderForUser(user_email, idNumOrder) {
    const email_name = user_email.split('@')[0];
    const userIdnumorder = ref(db, 'users/' + email_name + '/order/idnum');
    set(userIdnumorder, idNumOrder)
        .then(() => {
            console.log("id num order user successfully set in the database");
        })
        .catch((error) => {
            console.error("Error setting id num order user in the database:", error);
        });

}

// var geocoder = L.Control.geocoder({
//     defaultMarkGeocode: false
//   })
//     .on('markgeocode', function(e) {
//       var bbox = e.geocode.bbox;
//       var poly = L.polygon([
//         bbox.getSouthEast(),
//         bbox.getNorthEast(),
//         bbox.getNorthWest(),
//         bbox.getSouthWest()
//       ]).addTo(map);
//       map.fitBounds(poly.getBounds());
//     })
//     .addTo(map);

// var geocoder = L.Control.geocoder({
//     defaultMarkGeocode: true
// })
// .on('markgeocode', function(e) {
//     var bbox = e.geocode.bbox;

//     var distance = 0.005;
//     // Calculate expanded bounds by increasing the coordinates
//     var expandedBounds = L.latLngBounds(
//         [bbox.getSouthWest().lat - distance, bbox.getSouthWest().lng - distance],
//         [bbox.getNorthEast().lat + distance, bbox.getNorthEast().lng + distance]
//     );

//     var poly = L.polygon([
//         expandedBounds.getSouthEast(),
//         expandedBounds.getNorthEast(),
//         expandedBounds.getNorthWest(),
//         expandedBounds.getSouthWest()
//     ]).addTo(map);

//     map.fitBounds(poly.getBounds());
// })
// .addTo(map);
// var geocoder = L.Control.geocoder({
//     defaultMarkGeocode: true,
//     markers: marker // Pass the marker to the geocoder control
// }).addTo(map);