-- a script that creates the table force_name on your MySQL server.

-- create a table
CREATE TABLE IF NOT EXISTS id_not_null
(id INT NOT NULL DEFAULT 1, name VARCHAR(256));
