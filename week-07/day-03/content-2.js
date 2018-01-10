//fill every paragraph with the last one's content.
var theParagraph = document.querySelectorAll('p');
for(var i = 0; i < theParagraph.length; i++){
  theParagraph[i].innerHTML = theParagraph[3].innerHTML;
}