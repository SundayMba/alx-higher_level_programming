#!/usr/bin/env node
const request = require('request');
const titleId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${titleId}`;

request.get(url, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
