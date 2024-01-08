-- script that lists all the cities of California
-- that can be found in the database hbtn_0d_usa.

-- USE join instead of subqueries
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;

