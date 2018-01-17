'use strict'

var link = 'https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=New+York';

var button = document.querySelector('button');
button.addEventListener("click", linkBuilder);

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
        data = longitudeLatitude(data);
        console.log(data)
        coordinatesToGmaps(data)
      } else {
        console.log('There was a problem with the request.');
      }
    }
  }
}

function coordinatesToGmaps(data){
  var iframe = document.querySelector('iframe');
  return iframe.setAttribute('src', 'https://www.google.com/maps/embed/v1/view?key=AIzaSyDUkHnoCVVbEc60sTRY9jIR0mFH67kfUho&center=' + data + '&zoom=10" allowfullscreen')
}

function longitudeLatitude(data){
  var lonLat = data.Results[0].lat + ',' + data.Results[0].lon;
  var label = document.querySelector('label');
  return label.innerHTML = lonLat;
}

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




