/*1. Alert the content of the heading.
    2. Write the content of the first paragraph to the console.
    3. Alert the content of the second paragraph.
    4. Replace the heading's content with 'New content'.
    5. Replace the last paragraph's content with the first paragraph's content.*/
'use strict';
var heading = document.querySelector('h1');
//alert(heading.innerHTML)
var theParagraph = document.querySelectorAll('p');
console.log(theParagraph[0].innerHTML);
//alert(theFirstParagraph[1].innerHTML);
heading.textContent = 'New content';
theParagraph[2].textContent = theParagraph[0].innerHTML;
 