#!/usr/bin/env node
const fs = require('fs');
const arg = process.argv[2];

fs.readFile(arg, 'utf8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
