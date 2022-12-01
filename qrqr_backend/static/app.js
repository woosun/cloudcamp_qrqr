  // Initialize Firebase
  var config = {
    apiKey: "BHBcJLTFsZIYp9e6TFHbqJ7PRbhmvnxR8S2BBASR2wIW2xmkDSIs0AU6Ik_BwznRGlLm4LsxvHDD7pWOAyLiNgc",
    projectId: "qrqr-c2114",
    messagingSenderId: "748054356351"
  };
  firebase.initializeApp(config);

  const messaging = firebase.messaging();
  messaging.requestPermission().then(function() {
     //getToken(messaging);
     return messaging.getToken();
  }).then(function(token){
  console.log(token);
  })
.catch(function(err) {
  console.log('Permission denied', err);
});


messaging.onMessage(function(payload){
console.log('onMessage: ',payload);
});