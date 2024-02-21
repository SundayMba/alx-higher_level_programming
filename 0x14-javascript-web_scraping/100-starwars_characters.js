#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;
request.get(url, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;
    characters.forEach(character => {
      request.get(character, (error, res, body) => {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
