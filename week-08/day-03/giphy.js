'use strict';

/* let httpRequest = new XMLHttpRequest();
httpRequest.open('GET', 'http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=r7qmHjJcOc5BZnOR2a9W8SrdAwoDm3hY&limit=16', true); // Also try http://444.hu/feed
httpRequest.send();
httpRequest.onreadystatechange = console.log('yee')
var data = httpRequest.responseText;
data.setRequestHeader('Accept', 'image/*');
console.log(data);
 */



var http = new XMLHttpRequest();

http.open('GET', 'http://api.giphy.com/v1/gifs/search?q=power&api_key=r7qmHjJcOc5BZnOR2a9W8SrdAwoDm3hY&limit=16', true);
http.send();

function parser(freshData){
  freshData = JSON.parse(freshData)
  return freshData;
}
function applyToHtml(jsonObjects){
  for(var i = 0; i < jsonObjects.data.length; i++){
    var containImage = document.querySelector('.images');
    var image = document.createElement('img');
    containImage.appendChild(image);
    image.setAttribute('src', jsonObjects.data[i].images.downsized.url);
  }
}

http.onreadystatechange = function(){
  if (http.readyState === XMLHttpRequest.DONE) {
    console.log('done');
    if (http.status === 200) {
      console.log('status ok');
      var data = http.responseText;
      console.log(parser(data));
      data = parser(data);
      applyToHtml(data);
    } else {
      console.log('There was a problem with the request.');
    }
  }
}



