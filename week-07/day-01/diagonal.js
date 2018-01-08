'use strict';

var lineCount = 6;


// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

var draw = '%';
var space = ' ';
var length = 10;

console.log(draw.repeat(length + 2));
for(var i = 0; i < length; i++){
  console.log(draw + space.repeat(i) + draw + space.repeat(length - i - 1) + draw);
}
console.log(draw.repeat(length + 2));