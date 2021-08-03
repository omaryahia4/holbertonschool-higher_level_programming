#!/usr/bin/node
/* script that prints an integer convertable argument */
let argv = process.argv[2];
if (isNaN(argv) === true){
    console.log('Not a number');
}
else{
    console.log('My number: ' + argv);
}
