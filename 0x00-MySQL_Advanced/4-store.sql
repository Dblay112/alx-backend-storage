-- a script that creates a trigger to decrease item quantity
-- after a new order is added.

DROP TRIGGER IF EXISTS update_orders;
DELIMITER $$
CREATE TRIGGER update_orders
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$
DELIMITER ;
