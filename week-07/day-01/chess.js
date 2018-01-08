// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
//

var a = '%';
var b = " ";
var c = 10;
var d = 0;
while (d < c){
  console.log((a + b).repeat(4));
  console.log((b + a).repeat(4));
  d += 1;
}
