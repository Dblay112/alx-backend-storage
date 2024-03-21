-- script creates a trigger to update valid_email only
-- on email change


DROP TRIGGER IF EXISTS email_validator;
DELIMITER $$
CREATE TRIGGER email_validator
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
  END IF;
END;
