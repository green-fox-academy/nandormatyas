/*    1) replace the list items' content with items from this list:
    ['apple', 'banana', 'cat', 'dog']
    2) change the <ul> element's background color to 'limegreen'
      - don't just add a CSS class
      - use the .style attribute*/
'use strict';
var newItems = ['apple', 'banana', 'cat', 'dog'];
var listItems = document.querySelectorAll('li');
for(var i = 0; i < listItems.length; i++){
  listItems[i].innerHTML = newItems[i];
}
