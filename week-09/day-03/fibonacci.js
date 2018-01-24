'use strict';

const fibonacci1 = {
  fibonacci(n) {
    return n < 1 ? 0
         : n <= 2 ? 1
         : fibonacci1.fibonacci(n - 1) + fibonacci1.fibonacci(n - 2);
  },
};

module.exports = fibonacci1;
console.log(fibonacci1.fibonacci(10));
