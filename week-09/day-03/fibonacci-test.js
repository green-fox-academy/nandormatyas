'use strict';

const test = require('tape');
const fibonacci = require('./fibonacci.js');

class Test {
  constructor(actual, expected) {
    this.actual = actual;
    this.expected = expected;
  }
}

test('returns number of characters', function (t) {
  const ten = new Test(fibonacci.fibonacci(10), 55);

  t.equal(ten.actual, ten.expected);
  t.end();
});
