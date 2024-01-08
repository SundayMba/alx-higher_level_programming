-- a script that creates the database hbtn_0c_0 in your MySQL server.
-- update score using name col
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
