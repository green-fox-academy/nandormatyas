'use strict';

var fs = require('fs');
var musicData = require('musicmetadata');
var mysql = require('mysql');
var express = require('express');
var bodyParser = require('body-parser');
var cors = require('cors');

var app = express();
app.use(bodyParser.json());
app.use(express.urlencoded());
app.use(cors());

let conn = connectionDataSetup();
connectToMySQL();

function connectionDataSetup() {
  let conn = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '12345',
    database: 'songs',
  });
  return conn
};
function connectToMySQL () {
  conn.connect((err) => {
    if(err){
      console.log("Error connecting to Database");
      return;
    }
    console.log("Connection established");
    //fillDbWithSongs()
  });
};
function databaseError (err) {
  if(err) {
    console.log(err.toString());
    res.status(500).send('Database error');
    return;
  }
};


let audioFiles = fs.readdirSync('./songs/');

function fillDbWithSongs () {
  audioFiles.forEach(e => musicData(fs.createReadStream('./songs/' + e), {duration: true}, (err, metadata) => {
    if (err){
      console.log('Error happened')
    }
    let toSql = {
      'title': metadata.title,
      'author': metadata.artist,
      'duration': metadata.duration,
      'filename': e
    }
    conn.query('INSERT INTO songs SET ?', toSql, (err, result) => {
      databaseError();   
      console.log('saved');
    });
  }));
}

app.get('/songs', function(req, res) {
  conn.query('SELECT * FROM songs;', function(err, allSongs){
    databaseError();
    res.json(allSongs);
  });
});
  






app.listen(3000, function (){
  console.log('App is running');
});
