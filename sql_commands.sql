-- Create the main schema
CREATE SCHEMA IF NOT EXISTS ecommerce;

-- Create tables
CREATE TABLE ecommerce.users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ecommerce.products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ecommerce.orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    status ENUM('pending', 'shipped', 'delivered') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE ecommerce.order_items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Indexes for improved performance
CREATE INDEX idx_users_username ON ecommerce.users(username);
CREATE INDEX idx_products_price ON ecommerce.products(price);
CREATE INDEX idx_orders_user_id ON ecommerce.orders(user_id);
CREATE INDEX idx_order_items_product_id ON ecommerce.order_items(product_id);

-- Views for simplified querying
CREATE VIEW ecommerce.user_orders AS
SELECT u.username, o.order_id, o.total_amount, o.status
FROM users u
JOIN orders o ON u.user_id = o.user_id;

CREATE VIEW ecommerce.product_inventory AS
SELECT p.name, p.stock_quantity, p.price
FROM products p;

