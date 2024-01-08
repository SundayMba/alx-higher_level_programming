-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
-- specify database to work with

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
