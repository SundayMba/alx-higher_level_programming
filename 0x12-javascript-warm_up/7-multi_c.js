#!/usr/bin/node

let x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  x = Math.floor(Number(x));
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}

