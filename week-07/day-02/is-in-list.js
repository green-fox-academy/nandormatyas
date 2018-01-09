'use strict';
// Check if array contains all of the following elements: 4,8,12,16
// Create a 'numChecker' function that accepts 'listOfNumbers' as an input
// it should return "true" if it contains all, otherwise "false"

var listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 16];
var test_array = [ 4, 8, 12, 16 ];
var control_array =[];
function numChecker(array){
  for(var i = 0; i < array.length; i++){
    if(listOfNumbers.indexOf(array[i]) != -1){
      control_array.push(array[i])
    }
  }
  if(control_array.length == test_array.length){
    return true
  }else{
    return false
  }
}

console.log(numChecker(test_array))
