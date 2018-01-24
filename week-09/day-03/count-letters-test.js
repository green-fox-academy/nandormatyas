'use strict';

const test = require('tape');
const letters = require('./count-letters.js');

class Test {
  constructor(actual, expected) {
    this.actual = actual;
    this.expected = expected;
  }
}

test('returns number of characters', function (t) {
  const multiLetters = new Test(letters.letterCounter('alma'), { a: 2, l: 1, m: 1 });

  t.deepEqual(multiLetters.actual, multiLetters.expected);
  t.end();
});

test('returns number of characters', function (t) {
  const noLetters = new Test(letters.letterCounter(''), {});

  t.deepEqual(noLetters.actual, noLetters.expected);
  t.end();
});

test('returns number of characters', function (t) {
  const spaceLetters = new Test(letters.letterCounter('alma a'), { a: 3, l: 1, m: 1, ' ': 1 });

  t.deepEqual(spaceLetters.actual, spaceLetters.expected);
  t.end();
});


