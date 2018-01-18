'use strict'

var link = 'http://secure-reddit.herokuapp.com/simple/posts';

//var button = document.querySelector('button');
//button.addEventListener("click", linkBuilder);
function connectAndGetDataBackParsed(){
  var http = new XMLHttpRequest();
  http.open('GET', link, true);
  http.onreadystatechange = function(){
    if (http.readyState === XMLHttpRequest.DONE) {
      console.log('ready state: done');
      if (http.status === 200) {
        console.log('http status: ok');
        var data = http.responseText;
        data = JSON.parse(data).posts;
        console.log(data);
        threadCreator(data);
      } else {
        console.log('There was a problem with the request.');
      }
    }
  }
  http.send();
}
connectAndGetDataBackParsed()

function threadSetUp(){
  var forum = document.querySelector('.forum')
  var thread = document.createElement('div');
  forum.appendChild(thread);
  thread.setAttribute('class', 'thread');
}

function counterAndContentSetUp (index){

  var newThread = document.querySelectorAll('.thread');

  var counter = document.createElement('div');
  newThread[index].appendChild(counter);
  counter.setAttribute('class', 'counter');

  var content = document.createElement('div');
  newThread[index].appendChild(content);
  content.setAttribute('class', 'content');
}

function counterSetUp (index, data){
  
  var counter = document.querySelectorAll('.counter');

  var buttonUp = document.createElement('div');
  counter[index].appendChild(buttonUp);
  buttonUp.classList.add('button_up', 'index' + index);
  buttonUp.onclick = function () {
    let allScore = document.querySelectorAll('.score');
    let allButtonUp = document.querySelectorAll('.button_up');
      if(buttonUp.classList.item(1) === score.classList.item(1)){
        score.innerHTML++;
  
    }
}
  var score = document.createElement('div');
  counter[index].appendChild(score);
  score.classList.add('score', 'index' + index);
  score.innerHTML = data[index].score;

  var buttonDown = document.createElement('div');
  counter[index].appendChild(buttonDown);
  buttonDown.classList.add('button_down', 'index' + index);
}

function contentSetUp (index, data){
  
  var content = document.querySelectorAll('.content');

  var title = document.createElement('div');
  content[index].appendChild(title);
  title.setAttribute('class', 'title');
  title.innerHTML = data[index].title;

  var poster = document.createElement('div');
  content[index].appendChild(poster);
  poster.setAttribute('class', 'poster');
  if(data[index].user === null){
    poster.innerHTML = 'anonymous'
  }else{
    poster.innerHTML = data[index].user;
  }
  var timestamp = document.createElement('div');
  content[index].appendChild(timestamp);
  timestamp.setAttribute('class', 'timestamp');
  var inHours = data[index].timestamp;
  timestamp.innerHTML = inHours / 3600000;
}

function threadCreator (data){
  for(var i = 0; i < data.length;i++){
    threadSetUp(i);
    counterAndContentSetUp(i);
    counterSetUp(i, data);
    contentSetUp(i, data);
  }
}
//threadCreator(3)
function voter() {
  let allButtonDown = document.querySelectorAll('.button_down');
  let allScore = document.querySelectorAll('.score');
  let allButtonUp = document.querySelectorAll('.button_up');
}