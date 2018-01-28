'use strict';

//var link = 'https://time-radish.glitch.me/posts';
var link = 'http://localhost:3000/posts/';


var submitButton = document.querySelector('.submit_button');
submitButton.addEventListener("click", submit);

var postUser = document.querySelector('#user');  
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
  http.send(data);
}

function finalizeData() {
  var postText = document.querySelector('#to_post');
  var postUrl = document.querySelector('#url_name');
  var postUser = document.querySelector('#user');  
  var forSend = {
    'title': postText.value,
    'url': postUrl.value,
    'owner':postUser.value,
    'score': '0',
  }
  return forSend
}
function spammer(howMany) {
  for(var i = 0; i < howMany; i++){
    var data = {
      'title':'[nodemon] app crashed - waiting for file changes before starting...',
      'url': 'www.9gag.com',
      'owner': 'Tha Postman',
      'score': 0,
    }
    setInterval(postData(data), 1000);
  }
}
spammer(1)

function submit() {
  postData(finalizeData());
}
