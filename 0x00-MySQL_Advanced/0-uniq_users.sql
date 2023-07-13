-- Write a SQL script that creates a table users

CREATE TABLE IF NOT EXISTS users(
	id INT AUTO_INCREMENT NOT NULL, 
	email varchar(255) UNIQUE NOT NULL, 
	name varchar(255),
	PRIMARY KEY (id)
);
