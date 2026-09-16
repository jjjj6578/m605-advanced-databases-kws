import mysql.connector
import pymongo
from datetime import datetime, timedelta

def setup_mysql():
    print("Setting up MySQL Relational Tier...")
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jagruti@123"  # Update password if yours is different
    )
    cursor = conn.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS kws_relational_db;")
    cursor.execute("USE kws_relational_db;")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            client_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            coop_name VARCHAR(100),
            region VARCHAR(50)
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT AUTO_INCREMENT PRIMARY KEY,
            client_id INT,
            order_date DATE,
            total_amount DECIMAL(10, 2),
            FOREIGN KEY (client_id) REFERENCES clients(client_id)
        );
    """)

    # Insert 100+ records to satisfy assessment requirements
    cursor.execute("SELECT COUNT(*) FROM clients;")
    if cursor.fetchone()[0] < 100:
        regions = ["Central Europe", "Eastern Europe", "Scandinavia", "North America"]
        for i in range(1, 105):
            cursor.execute(
                "INSERT INTO clients (first_name, last_name, coop_name, region) VALUES (%s, %s, %s, %s);",
                (f"Grower_{i}", f"Manager_{i}", f"KWS Co-op Branch {i}", regions[i % len(regions)])
            )
            order_date = datetime.now() - timedelta(days=i)
            cursor.execute(
                "INSERT INTO orders (client_id, order_date, total_amount) VALUES (%s, %s, %s);",
                (i, order_date.strftime('%Y-%m-%d'), 150.00 + (i * 10))
            )
        conn.commit()
        print("Successfully generated 100+ records in MySQL!")
    
    cursor.close()
    conn.close()

def setup_mongodb():
    print("Setting up MongoDB NoSQL Tier...")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["kws_agricultural_db"]
    trial_logs = db["field_trial_logs"]
    
    if trial_logs.count_documents({}) < 100:
        trial_logs.delete_many({})
        log_batch = []
        crop_types = ["Corn", "Sugarbeet", "Winter Wheat", "Oilseed Rape"]
        
        for i in range(1, 105):
            log_batch.append({
                "trial_id": f"TR_2026_{i:03d}",
                "crop_type": crop_types[i % len(crop_types)],
                "plot_number": i,
                "soil_moisture_pct": 25.4 + (i % 5),
                "pest_resistance_rating": "High" if i % 2 == 0 else "Moderate"
            })
        trial_logs.insert_many(log_batch)
        print("Successfully generated 100+ documents in MongoDB!")

if __name__ == "__main__":
    setup_mysql()
    setup_mongodb()
    print("KWS Hybrid Database successfully initialized with 100+ records!")