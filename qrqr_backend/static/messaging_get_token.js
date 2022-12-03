  import { getMessaging, getToken } from "https://www.gstatic.com/firebasejs/9.14.0/firebase-messaging.js";
  const firebaseConfig = {
    apiKey: "AIzaSyBaqn2VoaA4-0nAQ55DX3FyF8hY92b3Zh4",
    authDomain: "qrqr-c2114.firebaseapp.com",
    projectId: "qrqr-c2114",
    storageBucket: "qrqr-c2114.appspot.com",
    messagingSenderId: "748054356351",
    appId: "1:748054356351:web:56b9b76bfc555b6c033a4a",
    measurementId: "G-687SWR2XS2"
  };
    const messaging = getMessaging();
getToken(messaging, { vapidKey: 'BHBcJLTFsZIYp9e6TFHbqJ7PRbhmvnxR8S2BBASR2wIW2xmkDSIs0AU6Ik_BwznRGlLm4LsxvHDD7pWOAyLiNgc' }).then((currentToken) => {
  if (currentToken) {
    console.log(currentToken)
  } else {
    console.log('No registration token available. Request permission to generate one.');
  }
}).catch((err) => {
  console.log('An error occurred while retrieving token. ', err);
});