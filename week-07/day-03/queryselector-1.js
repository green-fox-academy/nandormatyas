/*1. store the element that says 'The King' in the 'king' variable.
    console.log it.
    2. store the element that contains the text 'The Conceited Man'
    in the 'conceited' variable.
    show the result in an 'alert' window.
    3. store 'The Businessman' and 'The Lamplighter'
    in the 'businessLamp' variable.
    console.log each of them.
    4. store 'The King' and 'The Conceited Man'
    in the 'conceitedKing' variable.
    alert them one by one.
    5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
    in the 'noBusiness' variable.
    console.log each of them.
    6. store 'The Businessman' in the 'allBizniss' variable.
    show the result in an 'alert' window.*/
'use strict';
var king = document.getElementById('b325').innerHTML;
console.log(king);
var conceited = document.querySelector('.b326').innerHTML;
console.log(conceited);
var businessLamp = document.querySelectorAll('.big');
console.log(businessLamp[0].innerHTML, businessLamp[1].innerHTML);
var conceitedKing = [king, conceited];
//alert(king)
//alert(conceited)
var noBusiness = [king, conceited, businessLamp[1]];
console.log(noBusiness[0], noBusiness[1])
console.log(noBusiness[2].innerHTML);
var allBizniss = businessLamp[0].innerHTML;
alert(allBizniss);