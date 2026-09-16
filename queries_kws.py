import mysql.connector
import pymongo

def run_functional_queries():
    print("==============================================")
    print("  RUNNING KWS HYBRID DATABASE QUERIES & FLOW  ")
    print("==============================================\n")

    # --- 1. MYSQL RELATIONAL QUERY (Join & Retrieval) ---
    print("1. Executing MySQL Relational Query (Clients & Orders Join)...")
    try:
        mysql_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Jagruti@123",
            database="kws_relational_db"
        )
        cursor = mysql_conn.cursor()
        
        # Advanced query joining clients and their orders
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
            
        cursor.close()
        mysql_conn.close()
    except Exception as e:
        print(f"MySQL Query Error: {e}")

    print("\n----------------------------------------------\n")

    # --- 2. MONGODB NOSQL QUERY (Filter & Aggregation) ---
    print("2. Executing MongoDB NoSQL Query (Field Trial Logs Filter)...")
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["kws_agricultural_db"]
        trial_logs = db["field_trial_logs"]
        
        # Filter documents where crop type is 'Corn' and resistance is 'High'
        query_filter = {"crop_type": "Corn", "pest_resistance_rating": "High"}
        matched_docs = trial_logs.find(query_filter).limit(3)
        
        print("-> MongoDB Filter Results (Corn trials with High resistance):")
        for doc in matched_docs:
            print(f"   Trial ID: {doc.get('trial_id')} | Plot: {doc.get('plot_number')} | Soil Moisture: {doc.get('soil_moisture_pct')}%")
            
        # MongoDB Aggregation Pipeline: Average soil moisture per crop type
        print("\n-> MongoDB Aggregation Pipeline (Avg Soil Moisture by Crop):")
        pipeline = [
            {"$group": {"_id": "$crop_type", "avg_moisture": {"$avg": "$soil_moisture_pct"}}}
        ]
        agg_results = trial_logs.aggregate(pipeline)
        for agg in agg_results:
            print(f"   Crop: {agg['_id']} | Average Soil Moisture: {agg['avg_moisture']:.2f}%")
            
    except Exception as e:
        print(f"MongoDB Query Error: {e}")

    print("\n==============================================")
    print("  ALL FUNCTIONAL QUERIES EXECUTED SUCCESSFULLY")
    print("==============================================\n")

if __name__ == "__main__":
    run_functional_queries()