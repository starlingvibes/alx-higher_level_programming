-- creates a database and cities table
-- creating the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- using the database
USE hbtn_0d_usa;
-- creating the table
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY(id), FOREIGN KEY(state_id) REFERENCES states(id));
