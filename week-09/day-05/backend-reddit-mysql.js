'use strict';

var express = require('express');
var cors = require('cors');
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(express.urlencoded());
app.use(cors());



create table posts (id MEDIUMINT NOT NULL AUTOINCREMENT, title TEXT, url TEXT, timestamp MEDIUMINT, score MEDIUMINT, owner VARCHAR(30), PRIMARY KEY (id));