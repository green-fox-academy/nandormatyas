'use strict';
// - Create a variable named `ai` with the following content: `[3, 4, 5, 6, 7]`
// - Log the sum of the elements in `ai` to the console
var ai = [3, 4, 5, 6, 7];
function sumElements(array){
  var total = 0;
  for(var i = 0; i < array.length; i++){
    total += array[i];
  }
  return total
}
console.log(sumElements(ai))