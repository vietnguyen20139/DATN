
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import { getAuth, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-auth.js"
import { getDatabase, ref, startAt, onValue, set, onChildAdded, query, limitToLast, get, orderByChild, endAt, orderByKey } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-database.js";

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
const db = getDatabase();

// Initialize Firebase Authentication and get a reference to the service
const auth = getAuth(app);
var user_email = "";

export { user_email };
onAuthStateChanged(auth, (user) => {
  if (user) {
    // User is signed in, see docs for a list of available properties
    // https://firebase.google.com/docs/reference/js/auth.user
    const uid = user.uid;
    // alert("user is ", uid);
    user_email = user.email;
    console.log("user email in sing_out_state is ", user.email);
    updateUserEmail(user_email);

    createNewOrderEvent(user_email);
    updateTable();

    // createOrderID(user_email);
    // ...
  } else {
    // User is signed out
    // ...
    alert("User is signed out");

  }
});

// write user email to show user
function updateUserEmail(email) {
  const emailElement = document.getElementById('userEmail');
  if (emailElement) {
    emailElement.textContent = email;
  }
}

///////////////////////////////////// PASS DATA WHEN CREATE NEW ORDER
const createNewOrderBtn = document.getElementById("newOrderBtn");
// set useremail to the url when click neworderbutton 
function createNewOrderEvent(user_email) {
  // const email_name = user_email.split('@')[0];
  createNewOrderBtn.addEventListener('click', function () {
    var url = "./map_order.html?email=" + encodeURIComponent(user_email);
    window.open(url, "_blank");
  });
}

const btnSignout = document.getElementById('btnSignout');

// for sign out ///////////////////////////////////////////
// check if btnsignout exis, when open map order, it is not exis and error
if (btnSignout) {
  btnSignout.addEventListener('click', function (event) {
    auth.signOut().then(() => {
      console.log('User signed out!');
    });
  });
}

//////////////////////////////////////////////
function createOrderID(email) {
  const email_name = email.split('@')[0];
  const timestamp = Date.now();
  const orderId = `${email_name}${timestamp}`;
  // A timestamp represents a specific moment in time. In JavaScript, 
  //you can obtain the current timestamp using the Date.now() method or the new Date().getTime() method. 
  //Both methods return the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC (also known as the Unix epoch).
  console.log(orderId);
}

// //////////////////////////////////////////RETRIEVE OREDER TO TABLE
document.addEventListener('DOMContentLoaded', function () {
  console.log(document.location.pathname);
  if (window.location.pathname == "/user_page/user_main_no_sidebar.html") {
    console.log("in user main page");
    // updateTable();

  } else {
    // The current page is not the main page
    console.log('This is not the main page.');
  }
});



// const keyToGetForTableRow = ["dateCreateOrder", "orderID", "getDay", "typeContainer", "cargo1", "numsStop", "driver", "driverPhone", "car", "status"];
const keyToGetForTableRow = ["dateCreateOrder", "orderID", "getDay", "typeContainer", "cargo1", "numsStop", "driver", "car", "status"];

// "ngày tạo"          mã đơn   ngày chạy   loại cont       hàng hóa  số điểm dừng  tài xế    std driver    xe  trạng thái   

const table = document.getElementById('main_table');
const tbody = table.querySelector('tbody');

//9 col of key from firebase and 1 col of deletes
function updateTable() {
  const email_name = user_email.split('@')[0];
  console.log(email_name + " in update table")
  const orderRef = query(ref(db, "orders"), orderByKey(), startAt(email_name), endAt(`${email_name}\uf8ff`)); // use for limittolast
  //  \uf8ff represents the last possible character. By appending it to the query value, you ensure that the query includes all the keys that start with "220139049" and any subsequent characters.


  onChildAdded(orderRef, (snapshot) => {
  // onValue(orderRef, (snapshot) => {
  //   snapshot.forEach((childSnapshot) => {
      // onchildadded run for each child on orders, it run each order, if have 3 order 1,2,3 then run 1, then run 2, then run 3
      // console.log("oreder by email: " + snapshot.key); //key is orderID

      // USE WITH ONCHILDADDED
      const orderIdKeyFromFirebase = snapshot.key;
      const allValueOrder = snapshot.val(); // value contain all data 

      // USE WITH ONVALUE
      // const orderIdKeyFromFirebase = childSnapshot.key;
      // const allValueOrder = childSnapshot.val(); // value contain all data 

      console.log(orderIdKeyFromFirebase);
      // const value_data = value.address1;
      // console.log(value_data);
      const newRow = tbody.insertRow(); // Create a new row
      // add class for row to hide all row when need
      newRow.classList.add('main_table_row');

      keyToGetForTableRow.forEach(key => {
        var value = allValueOrder[key]; // Retrieve the value associated with each key
        // console.log(`${key}: ${value}`);

        if (value != null) {
          // process key = status to set value of status to running (number2) or complete (number3)
          if (key == "status") {
            // console.log(allValueOrder["datas"]);
            if (allValueOrder["datas"] != 0) {
              console.log("have data")
              value = 2;
            }

            if (allValueOrder["complete"] != 0) {
              console.log("completed")
              value = 3;
            }

            console.log("value of status is: " + value);
          }

          createRowOfTable(newRow, key, value, orderIdKeyFromFirebase);
        }
      });

      });
  //   });
  // });

}

function createRowOfTable(newRow, key, value, orderIdKeyFromFirebase) {
  var color = ["pending_color", "processed_color", "running_color", "completed_color", "canceled_color"]
  var status_cell = ["đang xử lý", "đã xử lý", "đang chạy", "đã chạy xong", "đã hủy"]
  var row_status = ["pending_row", "processed_row", "running_row", "completed_row", "canceled_row"]

  const newCell = newRow.insertCell();
  switch (key) {
    case "orderID":
      const tagLink = document.createElement('a');
      tagLink.href = 'javascript:void(0);';
      tagLink.target = "_blank";
      tagLink.textContent = value;

      // console.log(value);
      // set order id to value of orderid in firebase
      //add event click to taglink
      tagLink.addEventListener('click', function () {
        var url = "./order_information.html?order_id=" + encodeURIComponent(value);
        window.open(url, "_blank");
      });

      newCell.appendChild(tagLink);

      // create id for row as orderid to use for delete
      newRow.setAttribute("id", value);
      break;

    case "status":
      // console.log(typeof (value));
      // value is number, 0,1,2,3,4
      const tagLinkStatus = document.createElement('a');
      tagLinkStatus.href = 'javascript:void(0);';
      tagLinkStatus.target = "_blank";

      //add event click to taglink
      tagLinkStatus.addEventListener('click', function () {
        var url = "./map.html?order_id=" + encodeURIComponent(orderIdKeyFromFirebase);
        window.open(url, "_blank");
      });
      tagLinkStatus.textContent = status_cell[value];

      // add color to cell base on status
      newCell.classList.add(color[value]);
      // newCell.textContent = status_cell[value];

      // add tag to cell
      newCell.appendChild(tagLinkStatus);

      // add clast to row base on status to filter
      newRow.classList.add(row_status[value]);
      break;


    default:
      newCell.textContent = value;
      break;
  }
}

// //////////////////////////////////////////FILTER TABLE
const filterAllBtn = document.getElementById("all_order");
const filterPendingBtn = document.getElementById("pending_order");
const filterProcessedBtn = document.getElementById("processed_order");
const filterRunningBtn = document.getElementById("running_order");
const filterCompletedBtn = document.getElementById("completed_order");

// filter base on this class
// var row_status = ["pending_row", "processed_row", "running_row", "completed_row", "canceled_row"]

filterAllBtn.addEventListener('click', function () {
  const rows = document.getElementsByClassName('main_table_row');

  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];
    row.style.display = '';
  }
});

filterPendingBtn.addEventListener('click', function () {
  const rows = document.getElementsByClassName('main_table_row');

  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];

    if (!row.classList.contains('pending_row')) {
      row.style.display = 'none';
    } else {
      row.style.display = '';
    }
  }
});

filterProcessedBtn.addEventListener('click', function () {
  const rows = document.getElementsByClassName('main_table_row');

  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];

    if (!row.classList.contains('processed_row')) {
      row.style.display = 'none';
    } else {
      row.style.display = '';
    }
  }
});

filterRunningBtn.addEventListener('click', function () {
  const rows = document.getElementsByClassName('main_table_row');

  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];

    if (!row.classList.contains('running_row')) {
      row.style.display = 'none';
    } else {
      row.style.display = '';
    }
  }
});

filterCompletedBtn.addEventListener('click', function () {
  const rows = document.getElementsByClassName('main_table_row');

  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];

    if (!row.classList.contains('completed_row')) {
      row.style.display = 'none';
    } else {
      row.style.display = '';
    }
  }
});

