/*     Does the third p have a red-dot class?
    If so, alert 'OMG DOTS!'
    If the fourth p has a 'dolphin' class, replace apple's content with 'pear'
    If the first p has an 'apple' class, replace cat's content with 'dog'
    Make apple red by adding a .red class
    Make balloon less balloon-like
 */
'use-strict';
var theParagraphs = document.querySelectorAll('p');
if(theParagraphs[2].classList.contains('red-dot') === true){
  //alert('OMG DOTS!')
}
if(theParagraphs[3].classList.contains('dolphin') === true){
  document.querySelector('.apple').innerHTML = 'pear';
}
if(theParagraphs[0].classList.contains('apple') === true){
  document.querySelector('.cat').innerHTML = 'dog';
}
document.querySelector('.apple').classList.add('red');
ballonStyle = document.querySelector('.balloon');
ballonStyle.style['borderRadius'] = '5%' ;
