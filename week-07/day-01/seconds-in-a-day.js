'use strict';

var currentHours = 14;
var currentMinutes = 34;
var currentSeconds = 42;

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables

var hour = 3600;
var minute = 60;
var second = 1;
var day = 86400;

currentHours = hour * currentHours;
currentMinutes = minute * currentMinutes;
currentSeconds = second * currentSeconds;

var a = currentHours + currentMinutes + currentSeconds;
console.log(day - a);