'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds
console.log('apple'); // prints first
setTimeout(function() {
  console.log('pear'); // prints after one second
}, 1000);
setTimeout(function() {
  console.log('melon'); // prints after one second
}, 3000);
setTimeout(function() {
  console.log('grapes'); // prints after one second
}, 5000);