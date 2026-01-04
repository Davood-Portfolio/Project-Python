-- Sample customers
INSERT INTO customers (name, email) VALUES
('Ali Rezaei', 'ali@example.com'),
('Sara Ahmadi', 'sara@example.com'),
('Mehdi Karimi', 'mehdi@example.com');

-- Sample products
INSERT INTO products (name, price) VALUES
('Laptop', 1200.00),
('Mouse', 25.00),
('Keyboard', 45.00),
('Monitor', 300.00);

-- Sample orders
INSERT INTO orders (customer_id, order_date) VALUES
(1, '2026-01-01'),
(2, '2026-01-02'),
(3, '2026-01-03');

-- Sample order items
INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 1),
(3, 4, 1),
(3, 2, 1);
