-- ========================================================
-- KWS Hybrid Database: Analytical Queries & Operations
-- Database: kws_relational_db (MySQL 8.0)
-- ========================================================

USE kws_relational_db;

-- Query 1: Relational JOIN (Co-op sales reporting by region and order date)
SELECT 
    c.coop_name, 
    c.region, 
    o.order_date, 
    o.total_amount 
FROM clients c 
JOIN orders o ON c.client_id = o.client_id 
WHERE c.region = 'Eastern Europe'
LIMIT 5;

-- Query 2: Relational UPDATE (Applying price adjustment with ACID commit)
UPDATE orders 
SET total_amount = total_amount + 25.00 
WHERE client_id = 1;

-- Query 3: Regional Aggregation & Summary
SELECT 
    region, 
    COUNT(client_id) AS total_clients, 
    AVG(total_amount) AS avg_order_amount 
FROM clients c 
JOIN orders o ON c.client_id = o.client_id 
GROUP BY region;
