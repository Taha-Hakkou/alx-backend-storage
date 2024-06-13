-- 4-store.sql
-- creates a trigger that decreases the quantity of an item after adding a new order
CREATE TRIGGER decrease_quanitity
AFTER INSERT ON orders FOR EACH ROW
UPDATE SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
