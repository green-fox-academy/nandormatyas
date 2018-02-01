'use strict';

//let link = 'https://time-radish.glitch.me/posts';
let link = 'http://localhost:3000/login';


let submitButton = document.querySelector('.submit_button');
submitButton.addEventListener("click", function () {
  submit(link);
});
let loginButton = document.querySelector('.login_button');
loginButton.addEventListener('click', function () {
  login(link);
  
});

function postData(data, link){
  var http = new XMLHttpRequest();
  http.open('POST', link, true);
  http.setRequestHeader('Accept', 'application/json');
  http.setRequestHeader('Content-Type', 'application/json');
  http.setRequestHeader('Username', 'nemaBob');
  http.onreadystatechange = function(){
    if (http.readyState === XMLHttpRequest.DONE) {
      console.log('ready state: done');
      if (http.status === 200) {
        console.log('http status: ok');
        var data = http.responseText;
      }
    }
  }
  data = JSON.stringify(data);
  //console.log(data);
  http.send(data);
};

function finalizeData() {
  let userName = document.querySelector('#username');
  let password = document.querySelector('#password');
  let eMail = document.querySelector('#email');
  let forSend = {
    'username': userName.value,
    'password': password.value,
    'email':eMail.value,
  }
  return forSend
};

function submit(submitLink) {
  let link = submitLink + '/submit';
  planetFly();
  postData(finalizeData(), link);
};

function login (loginLink) {
  let link = loginLink + '/login';
  let user = finalizeData();
  delete user.email;
  console.log(user);
  postData(user, link);
};

function planetFly () {
  let planet = document.querySelector('.image');
  console.log(planet);
  planet.setAttribute('style', 'height: 1%;');
  console.log('bye planet');
}