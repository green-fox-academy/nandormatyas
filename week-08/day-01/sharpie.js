function Sharpie(color, width){
  this.color = color;
  this.width = width;
  this.inkAmount = 100;
  this.use = function(){
    this.inkAmount -= this.width;
  }
}
var pen = new Sharpie('red', 1);

function sharpieUser(writingTool){
  for(var i = 0; writingTool.inkAmount != 0 ; i++){
    writingTool.use();
  }
}
sharpieUser(pen);
