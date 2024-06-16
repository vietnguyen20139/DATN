
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-auth.js"
import { getDatabase, ref, set } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-database.js";

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

// Initialize Firebase Authentication and get a reference to the service
const auth = getAuth(app);

// Selecting radio buttons
const buttons = document.querySelectorAll("input[type='radio']");
const gender = 1;

// Adding event listener to all radio buttons

buttons.forEach(button => {
    button.addEventListener('click', () => {
        if (button.checked) {
            console.log(button.value + " selected as contact option!");
        }
    });
});

const btnSignup = document.getElementById('btnSignup');

// for sign up ///////////////////////////////////////////
btnSignup.addEventListener('click', function (event) {

    console.log("Sign Up");
    const email = document.getElementById('sign_up_email').value;
    const password = document.getElementById('sign_up_password').value;
    const passwordCheck = document.getElementById('sign_up_confirm_password').value;
    const name = document.getElementById('sign_up_get_name').value;
    const address = document.getElementById('sign_up_get_addr').value;
    const phone = document.getElementById('sign_up_get_phone').value;
    const selectElement = document.getElementById("gender");
    const selectedGender = selectElement.value;

    if (password !== passwordCheck) {
        alert("Xác nhận mật khẩu không khớp với Mật khẩu");
        return;
    }

    if (!email || !password || !passwordCheck || !name || !address || !phone) {
        // event.preventDefault();
        alert("Xin vui lòng điền đầy đủ vào tất cả các ô");
        return;
    }

    event.preventDefault()

    const username = email.split('@')[0];
    // console.log(typeof(username));
    // console.log(`users/${username}`);

    console.log(email, password, name, address, phone,);

    // Perform Firebase authentication or database query here
    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed up 

            const user = userCredential.user;

            // set data in firebase
            set(ref(database, `users/${username}`), {
                name: name,
                order: { idnum: 0, total: 0, wait: 0, processed: 0, running: 0, complete: 0 },
                email: email,
                address: address,
                phone: phone,
                gender: selectedGender
            })
                .then(() => {
                    console.log("Data successfully set in the database");

                    alert("Tạo tài khoản thành công");
                    window.location.href = "main_signin.html";
                })
                .catch((error) => {
                    alert("Lỗi tạo tài khoản: " + error);
                });
            // ...
        })
        .catch((error) => {
            // set something new_acc ] true
            const errorCode = error.code;
            const errorMessage = error.message;
            // alert(errorMessage);
            console.log(errorMessage);
            console.log(errorCode);

            alert("Lỗi: " + errorMessage);
            // ..
        });

    // Assuming you have initialized your Firebase Realtime Database and obtained the "database" reference
    // console.log(new_acc);

    // if (new_acc) {
    //     // Set the data in the "users" path with the username as the key
    //     set(ref(database, `users/${username}`), {
    //         name: name,
    //         email: email,
    //         address: address,
    //         phone: phone,
    //         gender: gender
    //     })
    //         .then(() => {
    //             console.log("Data successfully set in the database");
    //         })
    //         .catch((error) => {
    //             console.error("Error setting data in the database:", error);
    //         });
    // }
});


