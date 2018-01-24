'use strict';

const test = require('tape');
const apple = require('./apples.js');

test('return string: apple', function (t) {
  const actual = apple.getApple();
  const expected = 'apple';

  t.equal(actual, expected);
  t.end();
});
