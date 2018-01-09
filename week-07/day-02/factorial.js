'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(multiup){
  var total = 1;
  for(var i = 1; i <= multiup; i++){
    total *= i;
  }
  return total;
}
console.log(factorio(10));