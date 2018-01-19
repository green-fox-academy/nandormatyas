'use strict'

var link = 'https://time-radish.glitch.me/posts';

var submitButton = document.querySelector('.submit_button');
submitButton.addEventListener("click", submit);

var postUser = document.querySelector('#user');  
function postData(data){
  var http = new XMLHttpRequest();
  http.open('POST', link, true);
  http.setRequestHeader('Accept', 'application/json');
  http.setRequestHeader('Content-Type', 'application/json');
  http.setRequestHeader('Username', 'Rocky Balboa');
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
  }
  return forSend
}
function spammer(howMany) {
  for(var i = 0; i < howMany; i++){
    var data = {
      'title':'Iam luerat poenas frater Numitoris, et omne pastorum gemino sub duce vulgus erat Contrahere agrestes et moenia ponere utrique convenit. Ambigitur moenia ponat uter Nil opus est’ dixit ’certamine’ Romulus ’ullo: magna fides avium est, experiamur aves!’Res placet: Alter adit nemorosi saxa Palati ',
      'url': 'www.9gag.com',
    }
    setInterval(postData(data), 1000);
  }
}
//spammer(2)

function submit() {
  postData(finalizeData());
}
