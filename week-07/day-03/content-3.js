//    fill output1 with the first paragraph's content, text only.
//    fill output2 with the first paragraph's content keeping the cat strong.
var out1 = document.querySelectorAll('p');
out1[1].innerHTML = out1[0].innerHTML;
out1[2].innerHTML = out1[0].innerHTML;