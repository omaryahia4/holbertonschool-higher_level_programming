#!/usr/bin/node
let count = 0;
process.argv.forEach((val, index) => {
  count++;
});
if (count <= 2) {
    console.log('undefined is undefined');
}else if (count === 3) {
    console.log(process.argv[2] + ' is undefined');
}
else{
    console.log(process.argv[2] + ' is ' +  process.argv[3]);
}
