#!/usr/bin/node
/* fact */
function fact (n = 0) {
    if (n === 0) {
      return 1;
    } else {
      return n * fact(n - 1);
    }
  }
  console.log(fact(process.argv[2]));
