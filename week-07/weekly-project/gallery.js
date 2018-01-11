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
  addSmallImages.appendChild(image);
}
