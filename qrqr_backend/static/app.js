  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.14.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.14.0/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyBaqn2VoaA4-0nAQ55DX3FyF8hY92b3Zh4",
    authDomain: "qrqr-c2114.firebaseapp.com",
    projectId: "qrqr-c2114",
    storageBucket: "qrqr-c2114.appspot.com",
    messagingSenderId: "748054356351",
    appId: "1:748054356351:web:56b9b76bfc555b6c033a4a",
    measurementId: "G-687SWR2XS2"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);