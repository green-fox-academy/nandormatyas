'use strict';

var express = require('express');

var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(express.urlencoded());

app.post('/arrays', function (req, res) {
  if(req.body.what === 'sum'){
    let total = 0;
    for(let i = 0; i < req.body.numbers.length; i++){
      total += req.body.numbers[i];
    }
    res.json({
      "result": total,
    });
  }
  if(req.body.what === 'multiply'){
    let total = 1;
    for(let i = 0; i < req.body.numbers.length; i++){
      total *= req.body.numbers[i];
    }
    res.json({
      "result": total,
    });
  }
  if(req.body.what === 'double'){
    res.json({
      "result": req.body.numbers.map(i => i * 2),
    });
  }
});

app.listen(8080, function (){
  console.log('app is running');
});
