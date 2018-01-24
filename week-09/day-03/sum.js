'use strict';

const sumUp = {
  sumArray(array) {
    let all = 0;
    array.forEach(function(element) {
      if (typeof(element) === 'number') {
        all += element;
      }else{
        console.log('Only numbers are accepted. Please retry!')
      }
    });
    return all;
  }
}

module.exports = sumUp;
