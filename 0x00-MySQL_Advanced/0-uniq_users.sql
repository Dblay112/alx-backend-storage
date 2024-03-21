-- This script creates a table named 'users' in a MySQL database, ensuring it only 
-- occurs if the table doesn't already exist with the following requirements:
--  - id: Integer, not null, auto-incrementing primary key
--  - email: String (255 characters), not null, unique
--  - name: String (255 characters)

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
