#!/usr/bin/env node
const fs = require('fs');
const filename = process.argv[2];
const content = process.argv[3];

fs.writeFile(filename, content, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
