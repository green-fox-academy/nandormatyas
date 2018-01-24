'use strict';

const letters = {
  letterCounter(string) {
    let characters = {};
    string.split('').forEach(function(char) {
      characters[char] = (characters[char] || 0) + 1;
    });
    return characters
  },
};

module.exports = letters;
//console.log(letters.letterCounter('alma'));