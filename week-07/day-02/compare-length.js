'use strict';
// - Create a variable named `p1`
//   with the following content: `[1, 2, 3]`
// - Create a variable named `p2`
//   with the following content: `[4, 5]`
// - Log to the console if `p2` has more elements than `p1`
var p1 = [1, 2, 3];
var p2 = [4, 5];
if(p1.length > p2.length){
  console.log('p1 has more elements')
}else if(p1.length < p2.length){
  console.log('p2 has more elements')
}else{
  console.log('the two arrays are equal')
}