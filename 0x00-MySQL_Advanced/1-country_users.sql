-- this script creates a table users with the following requirements
-- been adhered to:
--  - id: Integer, not null, auto-incrementing primary key
--  - email: String (255 characters), not null, unique
--  - name: String (255 characters)
--  - country: Enumeration of countries (US, CO, TN), not null, default US

CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
