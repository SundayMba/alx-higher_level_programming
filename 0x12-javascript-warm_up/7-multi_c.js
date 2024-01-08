#!/usr/bin/node

let x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  x = Number(x);
  while (x) {
    console.log('C is fun');
    x--;
  }
}
