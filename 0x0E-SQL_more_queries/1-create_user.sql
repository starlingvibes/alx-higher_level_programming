-- create a new user with full privileges
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- granting the privileges
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
