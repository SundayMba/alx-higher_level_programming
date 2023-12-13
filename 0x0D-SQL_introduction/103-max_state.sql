-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
-- import dump file
source temperatures.sql

-- perform operation
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
