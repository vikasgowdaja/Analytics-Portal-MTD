import mysql.connector
from mysql.connector import Error
import sqlite3
import os
import pandas as pd
import time

# -----------------------------
# MySQL Configuration
# -----------------------------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "python",
    "database": "student_results",
    "port": 3306
}

# -----------------------------
# Function: Create Database if Missing
# -----------------------------
def create_database_if_not_exists():
    """Create MySQL database if it doesn't already exist."""
    print("🔍 Checking MySQL database existence...")
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            port=DB_CONFIG["port"]
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        print(f"✅ Database '{DB_CONFIG['database']}' is ready.")
    except Error as e:
        print(f"❌ Error creating database: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# -----------------------------
# Function: Save DataFrame to MySQL
# -----------------------------
def save_to_mysql(df):
    """Save the DataFrame into MySQL."""
    print("💾 Saving data to MySQL...")
    try:
        start = time.time()
        create_database_if_not_exists()

        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Department VARCHAR(50),
            Year VARCHAR(10),
            Semester VARCHAR(20),
            UniversitySeatNumber VARCHAR(20),
            StudentName VARCHAR(100),
            TotalInternalMarks INT,
            TotalExternalMarks INT,
            GrandTotalMarks INT
        )
        """)
        print("✅ Table 'results' verified/created.")

        insert_query = """
        INSERT INTO results 
        (Department, Year, Semester, UniversitySeatNumber, StudentName,
         TotalInternalMarks, TotalExternalMarks, GrandTotalMarks)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        for _, row in df.iterrows():
            cursor.execute(insert_query, (
                row.get("Department"),
                row.get("Year"),
                row.get("Semester"),
                row.get("University Seat Number"),
                row.get("Student Name"),
                int(row.get("Total Internal Marks", 0)),
                int(row.get("Total External Marks", 0)),
                int(row.get("Grand Total Marks", 0))
            ))

        connection.commit()
        print(f"✅ Inserted {len(df)} rows successfully into MySQL.")
        print(f"⏱️ Time taken: {time.time() - start:.2f} seconds")

    except Error as e:
        print(f"❌ Error saving data to MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 MySQL connection closed.")

# -----------------------------
# Function: Save DataFrame to SQLite
# -----------------------------
def save_to_local_sqlite(df, db_path="student_results.db"):
    """Save the entire DataFrame to a local SQLite (.db) file with dynamic schema."""
    print("💾 Saving data locally (SQLite)...")
    conn = None
    try:
        os.makedirs(os.path.dirname(db_path), exist_ok=True) if os.path.dirname(db_path) else None
        conn = sqlite3.connect(db_path)

        df_sql = df.copy()
        df_sql.columns = [col.replace(" ", "_") for col in df_sql.columns]

        df_sql.to_sql("results", conn, if_exists="replace", index=False)
        conn.commit()

        print(f"✅ Local SQLite copy saved at: {os.path.abspath(db_path)}")

    except Exception as e:
        print(f"❌ Error saving data to local SQLite: {e}")

    finally:
        if conn:
            conn.close()
            print("🔒 SQLite connection closed.")

# -----------------------------
# TEST (Run Directly)
# -----------------------------
if __name__ == "__main__":
    print("🐍 Running MySQL + SQLite integration test...\n")

    # Simple DataFrame for testing
    sample_data = {
        "Department": ["CSE", "ECE"],
        "Year": ["2024", "2024"],
        "Semester": ["6", "6"],
        "University Seat Number": ["USN001", "USN002"],
        "Student Name": ["Alice", "Bob"],
        "Total Internal Marks": [45, 50],
        "Total External Marks": [80, 78],
        "Grand Total Marks": [125, 128]
    }
    df = pd.DataFrame(sample_data)

    save_to_mysql(df)
    save_to_local_sqlite(df)
