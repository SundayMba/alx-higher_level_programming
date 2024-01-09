#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  for (let end = list.length - 1; end >= 0; end--) {
    reverse.push(list[end]);
  }
  return reverse;
};
