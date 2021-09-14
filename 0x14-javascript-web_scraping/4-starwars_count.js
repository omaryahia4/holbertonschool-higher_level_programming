#!/usr/bin/node
const fs = require('request');
const url = process.argv[2];
fs(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  let count = 0;

  for (const movie of data.results) {
    for (const char of movie.characters) {
      if (char.endsWith('/18/')) {
        count+=1;
      }
    }
  }

  console.log(count);
});