-- a script that creates the database hbtn_0c_0 in your MySQL server.
-- create a table and insert multiple rows
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- insert rows into the table
INSERT INTO second_table (id, name, score)
	VALUES
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8);
