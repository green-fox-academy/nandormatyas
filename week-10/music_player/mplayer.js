'use strict';

var link = 'http://localhost:3000/songs/';

function connectAndGetDataBackParsed(){
  var http = new XMLHttpRequest();
  http.open('GET', link, true);
  http.setRequestHeader('Accept', 'application/json');
  http.onreadystatechange = function(){
    if (http.readyState === XMLHttpRequest.DONE && http.status === 200) {
      console.log('ready state: done');
      console.log('http status: ok');
      var data = http.responseText;
      data = JSON.parse(data);
      console.log(data);
      allSongs(data);
    } else {
      console.log('There was a problem with the request.');
    };
  }
  http.send();
};
connectAndGetDataBackParsed();

function allSongs (data) {
  for(var i = 0; i < data.length;i++){
    songSetUp(data, i);
    colorPlaylist();
  };
};
function colorPlaylist () {
  let track = document.querySelectorAll('.song');
  for(let i = 0; i < track.length; i++){
    if(i % 2 === 0){
    track[i].style.background = 'lightgrey';  
    }else{
      track[i].style.background = 'rgb(128, 124, 124)';
    };
  };
};
function displayCurrentTrackData (data, index) {
  let currentTrack = document.querySelector('.info');
  currentTrack.innerHTML = data[index].author + '<br>' + data[index].title;
};

function songSetUp(data, index){
  
  let playlist = document.querySelector('.playlist');
  let songs = document.createElement('div');
  playlist.appendChild(songs);
  songs.classList.add('song', data[index].id);

  let title = document.createElement('div');
  songs.appendChild(title);
  title.classList.add('title');
  title.innerHTML = data[index].title + '(' + data[index].author + ')';

  let duration = document.createElement('div');
  songs.appendChild(duration);
  duration.classList.add('duration');
  let minutes = Math.floor(data[index].duration / 60);
  let seconds = data[index].duration - minutes * 60;
  duration.innerHTML = minutes + ':' + seconds;

  songs.onclick = function () {
    colorPlaylist();
    let audio = document.querySelector('audio');
    songs.setAttribute('style', 'background: green;');
    //let currentId = songs.classList.item(1);
    let source = document.getElementById('audio_source');
    source.src = 'songs/' + data[index].filename;
    displayCurrentTrackData(data, index);
    audio.load();
    audio.play();
    audio.addEventListener('ended', function () {
      nextTrack(data, index);
    });    
  };
};
function nextTrack (data, index) {
  index++
  let audio = document.querySelector('audio');
  let source = document.getElementById('audio_source');
  source.src = 'songs/' + data[index].filename;
  displayCurrentTrackData(data, index);
  colorPlaylist();
  //songs.setAttribute('style', 'background: green;');
  audio.load();
  audio.play();

}


