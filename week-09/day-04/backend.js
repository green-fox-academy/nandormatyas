'use strict';

var express = require('express');

var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(express.urlencoded());
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

app.get('/greeter', function (req, res) {
  if(req.query.name === undefined){
    res.json({
      "error": "Please provide a name!",
    });
  }else if (req.query.title === undefined){
    res.json({
      "error": "Please provide a title!",
    });
  }else{
    res.json({
      "welcome_message": "Oh, hi there " + req.query.name + ", my dear " + req.query.title + '!',
    })
  }
});

app.get('/appenda/:appendable', function (req, res) {
  res.json({
    "appended": req.params.appendable + 'a',
  });
});

app.post('/dountil/:what', function (req, res) {
  console.log(req.params.what);
  console.log(req.body.until);
  if(req.params.what === 'sum'){
    let total = 0;
    for(let i = 0; i <= req.body.until; i++){
      total += i;
    }
    res.json({
      "result": total,
    });
  }
  if(req.params.what === 'factor') {
    let total = 1;
    for(let i = 1; i <= req.body.until; i++){
      total *= i;
    }
    res.json({
      "result": total,
    });
  
  }
});


app.listen(8080, function (){
  console.log('app is running');
});
