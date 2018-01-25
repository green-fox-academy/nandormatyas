var express = require('express');

var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use('/assets', express.static('assets'));

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function (req, res) {
  if(req.query.input != undefined){
    let doubled = {
      "received": req.query.input,
      "result" : req.query.input * 2
    };
    res.json(doubled);
  }else{
    res.json({

    error: "Please provide an input!",
  });
  }
});

app.get('/greeter', )


app.listen(8080, function (){
  console.log('app is running');
});
