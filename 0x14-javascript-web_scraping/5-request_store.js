#!/usr/bin/node
const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];
req(url, function (err, response, body) {
  fs.writeFile(filename, body, 'utf8', function (err, data) {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
});
