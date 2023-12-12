-- a script that creates the database hbtn_0c_0 in your MySQL server.
-- update score using name col
SELECT score, name FROM second_table
WHERE name != 'NULL'
ORDER BY score DESC;
