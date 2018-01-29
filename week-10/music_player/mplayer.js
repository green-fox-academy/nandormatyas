'use strict';

var link = 'http://localhost:3000/posts/';

function connectAndGetDataBackParsed(){
  var http = new XMLHttpRequest();
  http.open('GET', link, true);
  http.setRequestHeader('Accept', 'application/json');
  http.onreadystatechange = function(){
    if (http.readyState === XMLHttpRequest.DONE && http.status === 200) {
      console.log('ready state: done');
      console.log('http status: ok');
      var data = http.responseText;
      data = JSON.parse(data).posts;
      console.log(data);
      threadCreator(data);
    } else {
      console.log('There was a problem with the request.');
    };
  }
  http.send();
}

function songsSetUp(index, data){
  var playlist = document.querySelector('.playlist');
  var songs = document.createElement('div');
  playlist.appendChild(songs);
  songs.classList.add('song'); 
};
