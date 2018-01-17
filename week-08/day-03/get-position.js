'use strict'
var link = 'https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=New+York';
function connectAndGetDataBack(){
  var http = new XMLHttpRequest();
  http.open('GET', link, true);
  http.setRequestHeader("X-Mashape-Key", "cDOGtM67remshwcWghm8d4hT5zzBp1arYiQjsn4REwX5xMDfYJ")
  http.setRequestHeader("Accept", "application/json");
  http.send();
  http.onreadystatechange = function(){
    if (http.readyState === XMLHttpRequest.DONE) {
      console.log('ready state: done');
      if (http.status === 200) {
        console.log('http status: ok');
        var data = http.responseText;
        data = parser(data);
        console.log(data);
      } else {
        console.log('There was a problem with the request.');
      }
    }
  }
}

var button = document.querySelector('button');
button.addEventListener("click", linkBuilder);

function getText(){
  var city = document.querySelector('input');
  return city.value
}

function linkBuilder(){
  var splitLink = link.split('=');
  splitLink[1] = '=' + getText();
  var linkToCity = splitLink.join('');
  link = linkToCity;
  connectAndGetDataBack();
}


function parser(freshData){
  freshData = JSON.parse(freshData)
  return freshData;
}



