'use strict';

var lineCount = 7;



// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is
var star = '*';
var space = ' ';
for(var i = 0; i < lineCount - 1; i++){
  console.log(space.repeat(lineCount - i) + star.repeat(2 * i + 1));
}
for(i; i >= 0; i--){
  console.log(space.repeat(lineCount - i) + star.repeat(2 * i + 1));
}


//for idx in range(n-1):
   // print((n-idx) * ' ' + (2*idx+1) * '*')
//for idx in range(n-1, -1, -1):
  //  print((n-idx) * ' ' + (2*idx+1) * '*')