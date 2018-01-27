var mysql = require('mysql');

var conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '12345',
  database: 'bookstore',

});

conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

conn.query('select * from author', function(err, result) {
  console.log(result);
});

conn.end();