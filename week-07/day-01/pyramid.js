'use strict';

var lineCount = 4;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

var pyramid = 10;

var space = " ";
var star = "*";
//a = 0;

for(var a = 0; a < pyramid; a++){
  console.log(space.repeat(pyramid - a - 1) + star.repeat(2 * a + 1));
}

//for (i in range(0, pyramid):
  //print( space * (pyramid - i -1) + star * (2 * i + 1))