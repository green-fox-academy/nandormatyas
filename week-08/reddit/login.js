'use strict';

//let link = 'https://time-radish.glitch.me/posts';
let link = 'http://localhost:3000/login';


let submitButton = document.querySelector('.submit_button');
submitButton.addEventListener("click", submit);

let loginButton = document.querySelector('.login_button');
loginButton.addEventListener('click', login);

function postData(data){
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
  console.log(data);
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

function submit() {
  postData(finalizeData());
  console.log(finalizeData());
};

function login () {
  let user = finalizeData();
  delete user.email;
  postData(user);
};