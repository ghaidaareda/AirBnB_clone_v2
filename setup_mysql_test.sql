-- prepares a MySQL server --

CREATE DATABASE IF Not EXISTS hbnb_test_db;

CREATE USER IF Not EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';