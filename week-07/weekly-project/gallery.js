var pictures = [
  {
    path: 'assets/castle.jpg',
    title: 'Castle',
    description: 'blablablablabla'
  },
  {
    path: 'assets/eclipse.jpg',
    title: 'Eclipse',
    description: 'blablablablabla'
  },
  {
    path: 'assets/garden.jpg',
    title: 'Garden',
    description: 'blablablablabla'
  },
  {
    path: 'assets/lagun.jpg',
    title: 'Lagun',
    description: 'blablablabla'
  },
  {
    path: 'assets/plane.jpg',
    title: 'Plane',
    description: 'blablablablabla'
  },
  {
    path: 'assets/wfall.jpg',
    title: 'Waterfall',
    description: 'blablablablabla'
  },
  {
    path: 'assets/moon.jpg',
    title: 'Moon',
    description: 'blablablablabla'
  },
]
var addSmallImages = document.querySelector('.small-images');

for(var i = 0; i < pictures.length; i++){
  var image = document.createElement('img');
  image.setAttribute('src', pictures[i].path);
  image.setAttribute('title', pictures[i].title);
  addSmallImages.appendChild(image);
}

var pathList = [];
for(var i = 0; i < pictures.length; i++){
  pathList.push(pictures[i].path);
}

document.querySelector('#main').setAttribute('src', pathList[0]);

var n = 0;
var buttonLeft = document.querySelector('.left');
buttonLeft.onmousedown = function(){
  document.querySelector('.left').style.background = 'green';
  document.querySelector('.left').style.boxShadow = 'inset -1px 2px 2px 1px black';
}
buttonLeft.onmouseup = function(){
  document.querySelector('.left').style.background = 'lightgray';
  document.querySelector('.left').style.boxShadow = '';
}
buttonLeft.onclick = function () {
  if(n - 1 === - 1 ){
    n = pathList.length - 1;
  }else{
    n -= 1;
  }
  document.querySelector('#main').setAttribute('src', pathList[n]);

}
var buttonRight = document.querySelector('.right');
buttonRight.onmousedown = function(){
  document.querySelector('.right').style.background = 'green';
  document.querySelector('.right').style.boxShadow = 'inset 1px 2px 2px 1px black';
}
buttonRight.onmouseup = function(){
  document.querySelector('.right').style.background = 'lightgray';
  document.querySelector('.right').style.boxShadow = '';
}
buttonRight.onclick = function () {
  if(n + 1 === pathList.length){
    n = 0;
  }else{
    n += 1;
  }
  document.querySelector('#main').setAttribute('src', pathList[n]);
}



