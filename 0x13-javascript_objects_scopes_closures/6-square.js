#!/usr/bin/node
const MySquare = require('./5-square');

module.exports = class Square extends MySquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let r = 0; r < this.height; r++) {
        let row = '';
        for (let col = 0; col < this.width; col++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
};
