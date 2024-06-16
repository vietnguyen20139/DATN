
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-auth.js"
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

// Initialize Firebase Authentication and get a reference to the service
const auth = getAuth(app);

const btnSignin = document.getElementById('btnSignin');

// // for sign in ///////////////////////////////////////////
// btnSignin.addEventListener('click', function (event) {
//     event.preventDefault()

//     const email = document.getElementById('sign_in_email').value;
//     const password = document.getElementById('sign_in_password').value;

//     if (email.leng)
//     signInWithEmailAndPassword(auth, email, password)
//         .then((userCredential) => {
//             // Signed in
//             const user = userCredential.user;
//             // ...
//             alert("sign in");
//             window.location.href = "../user_page/user_main_no_sidebar.html"
//         })
//         .catch((error) => {
//             const errorCode = error.code;
//             const errorMessage = error.message;
//             // alert(errorMessage);
//             alert("pass or email sai");
//         });
// });

btnSignin.addEventListener('click', function (event) {
    const email = document.getElementById('sign_in_email').value;
    const password = document.getElementById('sign_in_password').value;

    if (!email || !password) {
        // event.preventDefault();
        alert("Xin vui lòng điền đầy đủ vào tất cả các ô");
        return;
    }

    event.preventDefault();

    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed in
            const user = userCredential.user;
            // ...
            alert("Đăng nhập thành công");
            window.location.href = "../user_page/user_main_no_sidebar.html";
            // console.log(user.email);
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            alert("Sai email hoặc mật khẩu");
        });
});