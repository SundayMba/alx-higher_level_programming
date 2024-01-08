#!/usr/bin/node

let nums = process.argv;
if (nums.length <= 3) {
  console.log(0);
} else {
  nums = sortReverse(nums);
  console.log(nums[1]);
}

function sortReverse (n) {
  const arr = [];
  for (let i = 2; i < n.length; i++) {
    arr.push(Number(n[i]));
  }
  const len = arr.length;
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len - i - 1; j++) {
      if (arr[j] < arr[j + 1]) {
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
}
