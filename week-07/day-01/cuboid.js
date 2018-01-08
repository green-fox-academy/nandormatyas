'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

var length = 100;
var height = 200;
var width = 300;

var surface = (length + width + height) * 2;
var volume = length * width * height;

console.log('Surface: ' + surface);
console.log('Volume: ' + volume);
