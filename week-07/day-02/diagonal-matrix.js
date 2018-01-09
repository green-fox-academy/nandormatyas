'use strict';
// - Create (dynamically*) a two dimensional list
//   with the following matrix**. Use a loop!
//
//   0 0 0 1
//   0 0 1 0
//   0 1 0 0
//   1 0 0 0
//
// - Print this two dimensional list to the console
//
// * size should depend on a variable
// ** Relax, a matrix is just like an array
var size = 4;
var tile = 0;
var xline = [];
var yline = [];
for(var i = 0; i < size; i++){
  xline.push(0)
  for(var j = 0; j < size; j++){
    yline.push(0)
    }
  }
console.log(xline)
console.log(yline)
