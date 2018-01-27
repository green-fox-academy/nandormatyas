'use strict';

var mysql = require('mysql');
var express = require('express');
var bodyParser = require('body-parser');
var cors = require('cors');


var app = express();
app.use(bodyParser.json());
app.use(express.urlencoded());
app.use(cors());


var conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '12345',
  database: 'posts',
});

conn.connect((err) => {
  if(err){
    console.log("Error connecting to Database");
    return;
  }
  console.log("Connection established");
});

app.get('/posts', function(req, res) {
  conn.query('SELECT * FROM threads;',function(err, rows){
    if(err) {
      console.log(err.toString());
      res.status(500).send('Database error');
      return;
    }
    res.json({'posts': rows});
  });
});

app.post('/posts', function (req, res) {
  req.body.timestamp = Date.now() / 3600000;
  conn.query('INSERT INTO threads SET ?', req.body, (err, result) => {
    if(err) {
      console.log(err.toString());
      res.status(500).send('Database error');
      return;
    }
    console.log('saved')
    res.send();
  });
});

app.delete('/posts/:id', function (req, res) {
  conn.query('DELETE FROM threads WHERE id = ?', [req.params.id], (err, result) => {
    if(err) {
      console.log(err.toString());
      res.status(500).send('Database error');
      return;
    }
    console.log('deleted')
    res.send();
  });
});

app.put('/posts/:id/upvote', function (req, res) {
  conn.query('UPDATE threads SET score = ? WHERE id = ?', [req.body.score, req.body.id], (err, result) => {
    if(err) {
      console.log(err.toString());
      res.status(500).send('Database error');
      return;
    }
    console.log('upvoted')
    res.send();
  });  
});

app.put('/posts/:id/downvote', function (req, res) {
  conn.query('UPDATE threads SET score = ? WHERE id = ?', [req.body.score, req.body.id], (err, result) => {
    if(err) {
      console.log(err.toString());
      res.status(500).send('Database error');
      return;
    }
    console.log('downvoted')
    res.send();
  });
});
app.listen(3000, function (){
  console.log('app is running');
});

/* conn.end(function () {
  console.log('SQL Connection ended')
});
 */