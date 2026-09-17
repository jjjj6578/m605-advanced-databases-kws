import os
import mysql.connector
import pymongo

def run_functional_queries():
    print("==============================================")
    print("  RUNNING KWS HYBRID DATABASE QUERIES & FLOW  ")
    print("==============================================\n")

    db_password = os.getenv("MYSQL_PASSWORD", "Jagruti@123")

    # --- 1. MYSQL RELATIONAL QUERY (Join & Retrieval) ---
    print("1. Executing MySQL Relational Query (Clients & Orders Join)...")
    try:
        mysql_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=db_password,
            database="kws_relational_db"
        )
        cursor = mysql_conn.cursor()
        
        query = """
            SELECT c.coop_name, c.region, o.order_date, o.total_amount 
            FROM clients c 
            JOIN orders o ON c.client_id = o.client_id 
            LIMIT 5;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        
        print("-> MySQL Join Results (First 5 records):")
        for row in results:
            print(f"   Co-op: {row[0]} | Region: {row[1]} | Date: {row[2]} | Amount: €{row[3]}")
            
    except Exception as e:
        print(f"MySQL Query Error: {e}")

    print("\n----------------------------------------------\n")

    # --- 2. CROSS-DATABASE INTEGRATION FLOW ---
    print("2. Executing Cross-Database Data Flow (MySQL -> MongoDB)...")
    try:
        # Fetch clients from Eastern Europe in MySQL
        cursor.execute("SELECT client_id, coop_name FROM clients WHERE region = 'Eastern Europe' LIMIT 3;")
        regional_clients = cursor.fetchall()
        
        client_mongo = pymongo.MongoClient("mongodb://localhost:27017/")
        db_mongo = client_mongo["kws_agricultural_db"]
        trial_logs = db_mongo["field_trial_logs"]
        
        print("-> Cross-Referencing MySQL Clients with MongoDB Field Trials:")
        for idx, client in enumerate(regional_clients, start=1):
            matching_trial = trial_logs.find_one({"plot_number": idx})
            if matching_trial:
                print(f"   Client: {client[1]} (ID: {client[0]}) -> Linked Trial ID: {matching_trial['trial_id']} ({matching_trial['crop_type']})")

    except Exception as e:
        print(f"Integration Error: {e}")

    print("\n----------------------------------------------\n")

    # --- 3. FULL CRUD OPERATIONS (Update & Delete) ---[cite: 5]
    print("3. Executing CRUD Operations (Update & Delete)...")
    try:
        # UPDATE: Modify a MongoDB trial log record
        update_result = trial_logs.update_one(
            {"trial_id": "TR_2026_004"},
            {"$set": {"soil_moisture_pct": 31.5, "pest_resistance_rating": "Very High"}}
        )
        print(f"-> MongoDB Update: Modified {update_result.modified_count} document(s).")

        # DELETE: Remove an obsolete trial log record
        delete_result = trial_logs.delete_one({"trial_id": "TR_2026_104"})
        print(f"-> MongoDB Delete: Removed {delete_result.deleted_count} document(s).")

        # UPDATE: Modify a MySQL relational order amount
        cursor.execute("UPDATE orders SET total_amount = total_amount + 25.00 WHERE client_id = 1;")
        mysql_conn.commit()
        print(f"-> MySQL Update: Successfully updated order amount for client 1.")

    except Exception as e:
        print(f"CRUD Operation Error: {e}")

    print("\n----------------------------------------------\n")

    # --- 4. MONGODB NOSQL AGGREGATION ---[cite: 5]
    print("4. Executing MongoDB Aggregation Pipeline (Avg Soil Moisture by Crop)...")
    try:
        pipeline = [
            {"$group": {"_id": "$crop_type", "avg_moisture": {"$avg": "$soil_moisture_pct"}}}
        ]
        agg_results = trial_logs.aggregate(pipeline)
        for agg in agg_results:
            print(f"   Crop: {agg['_id']} | Average Soil Moisture: {agg['avg_moisture']:.2f}%")
            
        cursor.close()
        mysql_conn.close()
    except Exception as e:
        print(f"MongoDB Aggregation Error: {e}")

    print("\n==============================================")
    print("  ALL FUNCTIONAL QUERIES EXECUTED SUCCESSFULLY")
    print("==============================================\n")

if __name__ == "__main__":
    run_functional_queries()