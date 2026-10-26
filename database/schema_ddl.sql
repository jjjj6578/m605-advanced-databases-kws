-- ========================================================
-- KWS Hybrid Database: Relational Tier DDL & Schema Setup
-- Database: kws_relational_db (MySQL 8.0)
-- ========================================================

CREATE DATABASE IF NOT EXISTS kws_relational_db;
USE kws_relational_db;

-- Drop tables if resetting environment
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS clients;

-- 1. Clients Table (Co-op branch accounts)
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    coop_name VARCHAR(100) NOT NULL,
    region VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

-- 2. Orders Table (Sales transactions with foreign key constraint)
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    CONSTRAINT fk_client_order 
        FOREIGN KEY (client_id) 
        REFERENCES clients(client_id) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ========================================================
-- Index Optimization for Performance
-- ========================================================
CREATE INDEX idx_region ON clients(region);
CREATE INDEX idx_client_fk ON orders(client_id);
