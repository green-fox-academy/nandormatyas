/*     On the click of the button,
    Count the items in the list
    And display the result in the result element.
 */
var button = document.querySelector('button');
button.onclick = function(){
  var listItems = document.querySelectorAll('li');
  var itemPieces = listItems.length;
  
  var result = document.querySelector('.result');
  result.innerHTML = itemPieces;
}


