#!/usr/bin/node
/* script that prints x times “C is fun” */
if (process.argv.length < 3) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < process.argv[2]; i++) {
      console.log('C is fun');
    }
  }
