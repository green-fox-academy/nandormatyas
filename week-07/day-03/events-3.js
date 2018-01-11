/*  1) Subscibe to keyup events on the global window object
    2) Console log the event object and peek inside
    3) Display the last pressed key's code as "Last pressed key code is: __"
 */
document.onkeypress = function(event){
  event = window.event;
  var charCode = event.keyCode;
  var charString = String.fromCharCode(charCode);
  document.querySelector('h1').textContent = 'Last pressed key is: ' + charString;
}