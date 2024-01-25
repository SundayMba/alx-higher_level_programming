-- create a database if it does not exist
CREATE DATABASE IF NOT EXISTS testdb;

-- switch to the created db
USE testdb

CREATE TABLE IF NOT EXISTS user (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
	);

INSERT INTO user (name) VALUES ('california'), ('Arizona'), ('Texa'), ('New York');
