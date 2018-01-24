'use strict';

const test = require('tape');
const anagramFunc = require('./anagram.js');

class Test {
  constructor(actual, expected) {
    this.actual = actual;
    this.expected = expected;
  }
}

test('return if anagram or not', function (t) {
  const notAnagram = new Test(anagramFunc.checkIfAnagram('abcdefg', 'gfdbac'), false);

  t.equal(notAnagram.actual, notAnagram.expected);
  t.end();
});

test('return if anagram or not', function (t) {
  const anagram = new Test(anagramFunc.checkIfAnagram('abcdefg', 'gfdbace'), true);

  t.equal(anagram.actual, anagram.expected);
  t.end();
});


