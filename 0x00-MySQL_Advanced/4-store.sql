-- creates a trigger that decreases the quantity
-- of an item after adding a new order.

CREATE TRIGGER myTrigger
AFTER INSERT ON orders FOR EACH ROW
UPDATE items
SET quantity = quantity-New.number
WHERE name=New.item_name;
