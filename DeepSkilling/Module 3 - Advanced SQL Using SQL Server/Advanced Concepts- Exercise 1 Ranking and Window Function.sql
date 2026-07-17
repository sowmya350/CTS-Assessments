CREATE DATABASE IF NOT EXISTS shop_db;
USE shop_db;

DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

INSERT INTO products (product_name, category, price) VALUES
('iPhone 15', 'Mobile', 799.00),
('Samsung S24', 'Mobile', 899.00),
('OnePlus 12', 'Mobile', 699.00),
('Pixel 8', 'Mobile', 699.00),
('Dell XPS 13', 'Laptop', 1299.00),
('MacBook Air', 'Laptop', 1199.00),
('HP Spectre', 'Laptop', 1299.00),
('Lenovo Yoga', 'Laptop', 1099.00),
('Sony WH-1000XM5', 'Headphones', 399.00),
('Bose QC Ultra', 'Headphones', 429.00),
('AirPods Max', 'Headphones', 549.00),
('JBL Tour One', 'Headphones', 299.00);

WITH ranked_products AS (
    SELECT
        product_id,
        product_name,
        category,
        price,
        ROW_NUMBER() OVER (
            PARTITION BY category
            ORDER BY price DESC
        ) AS row_num,
        RANK() OVER (
            PARTITION BY category
            ORDER BY price DESC
        ) AS rank_num,
        DENSE_RANK() OVER (
            PARTITION BY category
            ORDER BY price DESC
        ) AS dense_rank_num
    FROM products
)
SELECT *
FROM ranked_products
WHERE row_num <= 3
ORDER BY category, row_num;

WITH ranked_products AS (
    SELECT
        product_id,
        product_name,
        category,
        price,
        ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) AS row_num,
        RANK() OVER (PARTITION BY category ORDER BY price DESC) AS rank_num,
        DENSE_RANK() OVER (PARTITION BY category ORDER BY price DESC) AS dense_rank_num
    FROM products
)
SELECT *
FROM ranked_products
ORDER BY category, price DESC, product_name;