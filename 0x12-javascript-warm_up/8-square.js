#!/usr/bin/node
/* script that prints a square */
if (process.argv.length < 2 || isNaN(process.argv[2])) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < process.argv[2]; i++) {
      console.log('X'.repeat(process.argv[2]));
    }
  }