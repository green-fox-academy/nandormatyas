'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(until){
  var total = 0;
    for(var i = 0; i <= until; i++){
      total += i;
    }
    return total;
}
console.log(sum(10));