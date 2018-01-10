/*  Add an item that says 'The Green Fox' to the asteroid list.
    Add an item that says 'The Lamplighter' to the asteroid list.
    Add a heading saying 'I can add elements to the DOM!' to the .container.
    Add an image, any image, to the container.
 */
'use strict';

var asteroidList = document.querySelector('.asteroids');
var newListElement = document.createElement('li');
newListElement.innerHTML = 'The Green Fox';
asteroidList.appendChild(newListElement);

var lamplighter = document.createElement('li');
asteroidList.appendChild(lamplighter);
lamplighter.innerHTML = 'Lamplighter';

var heading = document.createElement('h1');
heading.innerHTML = 'I can add elements to the DOM!';
document.querySelector('body').appendChild(heading);

var containImage = document.querySelector('.container');
var image = document.createElement('img');
containImage.appendChild(image);
image.setAttribute('src', 'D:\smallsnake.jpg');