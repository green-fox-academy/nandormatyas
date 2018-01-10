/*     Remove the Mega juicy candy from the list.
    Add 16 list items saying 'Empty box' to the list and add an index to it, like:
    Empty box #1
    Empty box #2
    Empty box #3
    ...
 */
var theCandyShop = document.querySelector('.candyshop');
var child = document.querySelector('li');
var removed = theCandyShop.removeChild(child);

var index = 1;
for(var i = 0; i < 16; i++){
  var emptyBox = document.createElement('li');
  theCandyShop.appendChild(emptyBox);
  emptyBox.innerHTML = 'Empty box ' + '#' + index;
  index += 1;
}