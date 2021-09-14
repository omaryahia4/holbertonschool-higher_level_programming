#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];
request(url, function (errr, response, body) {
  fs.writeFile(filename, body, 'utf8', function (err, data) {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
});
