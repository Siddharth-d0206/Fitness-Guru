// static/js/firebase.js
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
import { getFirestore, collection, addDoc } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCSs8RlFLTXofnvUcYYgoTFulJtGppWiBI",
    authDomain: "fitnessai-5ffc4.firebaseapp.com",
    projectId: "fitnessai-5ffc4",
    storageBucket: "fitnessai-5ffc4.appspot.com",
    messagingSenderId: "175181615870",
    appId: "1:175181615870:web:09ab675705e2b175c8cbaf",
    measurementId: "G-XTNEB3TBC3"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth();
const db = getFirestore(app);

export { auth, db, createUserWithEmailAndPassword, signInWithEmailAndPassword, collection, addDoc };
