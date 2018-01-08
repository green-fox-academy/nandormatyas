'use strict';

var lineCount = 6;

// Write a program that draws a
// square like this:
//
//
// %%%%%
// %   %
// %   %
// %   %
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

var side = '%';
var space = ' ';
var length = 6;

console.log(side.repeat(length));
for(var i = 0; i <= length; i++){
  console.log(side + space.repeat(length - 2) + side);
}
console.log(side.repeat(length));