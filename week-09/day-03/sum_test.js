'use strict';

'use strict';

const test = require('tape');
const sum = require('./sum.js');

class Test {
  constructor(actual, expected) {
    this.actual = actual;
    this.expected = expected;
  }
}

test('return sum of array', function (t) {
  const emptyList = new Test(sum.sumArray([]), 0)

  t.equal(emptyList.actual, emptyList.expected);
  t.end();
});

test('return sum of array', function (t) {
  const oneElementList = new Test(sum.sumArray([5]), 5);

  t.equal(oneElementList.actual, oneElementList.expected);
  t.end();
});

test('return sum of array', function (t) {
  const manyElementList = new Test(sum.sumArray([5, 6, 8, 11, 2]),32);

  t.equal(manyElementList.actual, manyElementList.expected);
  t.end();
});

test('return sum of array', function (t) {
  const nullElementList = new Test(sum.sumArray([null]), 0);

  t.equal(nullElementList.actual, nullElementList.expected);
  t.end();
});

test('return sum of array', function (t) {
  const stringElementList = new Test(sum.sumArray(['alma']), 0);

  t.equal(stringElementList.actual, stringElementList.expected);
  t.end();
});



