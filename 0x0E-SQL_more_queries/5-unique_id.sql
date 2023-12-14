-- a script that creates the table force_name on your MySQL server.

-- create a table
CREATE TABLE IF NOT EXISTS unique_id
(id INT NOT NULL DEFAULT 1 UNIQUE, name VARCHAR(256));
