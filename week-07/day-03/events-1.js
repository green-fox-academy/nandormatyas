/*     Turn the party on and off by clicking the button. (the whole page)
 */
var button = document.querySelector('button');
var division = document.querySelector('div');
button.onclick = function(){
  if(division.className == 'party'){
    division.setAttribute('class', '');
  }else{
    division.setAttribute('class', 'party');
  }
}


if(theParagraphs[3].classList.contains('dolphin') === true){
  document.querySelector('.apple').innerHTML = 'pear';
}