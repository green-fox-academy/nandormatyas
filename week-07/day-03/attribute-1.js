/*     Write the image's url to the console.
    Replace the image with a picture of your favorite animal.
    Make the link point to the Green Fox Academy website.
    Disable the second button.
    Replace its text with 'Don't click me!'.
 */
var imageUrl = document.querySelector('img');
console.log(imageUrl.src)
imageUrl.src = 'D:\smallsnake.jpg';
var reLink = document.querySelector('a');
reLink.href = 'https://www.greenfoxacademy.com/'
var button = document.querySelectorAll('button');
button[1].setAttribute('class', "");
button[1].innerHTML = 'Don\'t click me';