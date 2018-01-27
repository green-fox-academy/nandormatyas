'use strict';
var mysql = require('mysql');
var express = require('express');
var app = express();


var conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '12345',
  database: 'bookstore',

});


app.get('/', function(req, res) {
  conn.query('SELECT book_name FROM book_mast;',function(err,rows){
    if(err) {
      console.log(err.toString());
      res.satus(500).send('Database error');
      return;
    }
    res.send(rows);
  });
});
app.listen(3000);