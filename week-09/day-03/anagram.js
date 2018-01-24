'use strict';

const stringCheck = {
  checkIfAnagram(string1, string2) {
    if (!string1 || !string2 || string1.length !== string2.length) {
      return false;
    }

    const lstring1 = string1.toLowerCase();
    const lstring2 = string2.toLowerCase();

    if (lstring1 === lstring2) {
      return false;
    }

    const rstring1 = lstring1.split('').sort().join('');
    const rstring2 = lstring2.split('').sort().join('');

    return rstring1 === rstring2;
  },
};
module.exports = stringCheck;
