-- script that lists all the cities of California
-- that can be found in the database hbtn_0d_usa.

-- USE join instead of subqueries
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

