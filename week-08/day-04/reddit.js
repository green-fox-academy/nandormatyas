'use strict'

var link = 'https://time-radish.glitch.me/posts';

//var button = document.querySelector('button');
//button.addEventListener("click", linkBuilder);
function connectAndGetDataBackParsed(){
  var http = new XMLHttpRequest();
  http.open('GET', link, true);
  http.send();
  http.onreadystatechange = function(){
    if (http.readyState === XMLHttpRequest.DONE) {
      console.log('ready state: done');
      if (http.status === 200) {
        console.log('http status: ok');
        var data = http.responseText;
        data = JSON.parse(data);
        console.log(data)
      } else {
        console.log('There was a problem with the request.');
      }
    }
  }
}
//connectAndGetDataBackParsed();
function threadSetUp(){
  var forum = document.querySelector('.forum')
  var thread = document.createElement('div');
  forum.appendChild(thread);
  thread.setAttribute('class', 'thread');
}

function counterAndContentSetUp (index){
  //var index = 1;

  var newThread = document.querySelectorAll('.thread');

  var counter = document.createElement('div');
  newThread[index].appendChild(counter);
  counter.setAttribute('class', 'counter');

  var content = document.createElement('div');
  newThread[index].appendChild(content);
  content.setAttribute('class', 'content');
}

function counterSetUp (index){
  //var index = 1;
  
  var counter = document.querySelectorAll('.counter');

  var buttonUp = document.createElement('div');
  counter[index].appendChild(buttonUp)
  buttonUp.setAttribute('class', 'button_up');

  var score = document.createElement('div');
  counter[index].appendChild(score)
  score.setAttribute('class', 'score');

  var buttonDown = document.createElement('div');
  counter[index].appendChild(buttonDown)
  buttonDown.setAttribute('class', 'button_down');
}

function contentSetUp (index){
  //var index = 1;
  
  var content = document.querySelectorAll('.content');

  var title = document.createElement('div');
  content[index].appendChild(title)
  title.setAttribute('class', 'title');

  var poster = document.createElement('div');
  content[index].appendChild(poster)
  poster.setAttribute('class', 'poster');

  var timestamp = document.createElement('div');
  content[index].appendChild(timestamp)
  timestamp.setAttribute('class', 'timestamp');
}

function threadCreator (data){
  for(var i = 1; i < data;i++){
    threadSetUp(i);
    counterAndContentSetUp(i);
    counterSetUp(i);
    contentSetUp(i);
  }
}
threadCreator(3)

