-- creates a database and a table on a MySQL server
-- creating the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- using the database
USE hbtn_0d_usa;
-- creating the table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
