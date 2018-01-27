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


app.listen(3000, function (){
  console.log('app is running');
});

/* conn.end(function () {
  console.log('SQL Connection ended')
});
 */

/* conn.query('INSERT INTO threads (title) VALUES (\'Kisherceg\'), (\'Robinson crusoe\')', (err, result) => {
  getTableElements();
  console.log(result);
});
 */
/* conn.query('UPDATE threads SET score = 2 WHERE title = \'Kisherceg\' AND thread_id = 18;', (err, result) => {
  console.log('changed');
});
 */

/* conn.query('DELETE FROM threads WHERE title = \'Kisherceg\' AND thread_id > 10', (err, result) => {
  console.log(result);
});
 */

