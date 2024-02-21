#!/usr/bin/env node
const request = require('request');
const url = process.argv[2];

const completedTask = {};
request.get(url, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    tasks.forEach(task => {
      if (task.completed) {
        if (completedTask[task.userId]) {
          completedTask[task.userId] += 1;
        } else {
          completedTask[task.userId] = 1;
        }
      }
    });
    console.log(completedTask);
  }
});
