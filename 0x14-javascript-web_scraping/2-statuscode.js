#!/usr/bin/node
const fs = require('request');
fs(process.argv[2], function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
