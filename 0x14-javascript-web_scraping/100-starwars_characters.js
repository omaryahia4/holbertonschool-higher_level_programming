#!/usr/bin/node
const fs = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
fs(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  for (const char of data.characters) {
    fs(char, function (err, response, body) {
      console.log(JSON.parse(body).name);
    });
  }
});