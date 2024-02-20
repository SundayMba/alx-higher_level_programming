#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

let count = 0;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body);
    movies.results.forEach(movie => {
      movie.characters.forEach(c => {
        if (c.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
