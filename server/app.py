from datetime import datetime
import os
import pandas as pd
from helper import extract_data_from_folder
from db import save_to_mysql, save_to_local_sqlite

def process_today_data():
    today_str = datetime.now().strftime("%d-%m-%Y")
    folder_path = os.path.join("./uploads", today_str)
    csv_output_file = f"./output/result_{today_str}.csv"
    db_path = f"./output/student_results_{today_str}.db"

    print(f"📁 Checking folder: {folder_path}")

    if not os.path.exists(folder_path):
        print("❌ Folder not found:", folder_path)
        return None

    # Delete old CSV & DB only
    if os.path.exists(csv_output_file):
        os.remove(csv_output_file)
        print("🗑️ Deleted old CSV")

    if os.path.exists(db_path):
        os.remove(db_path)
        print("🗑️ Deleted old DB")

    df = extract_data_from_folder(folder_path)

    if df.empty:
        print("⚠️ No data extracted.")
        return None

    os.makedirs("./output", exist_ok=True)
    df.to_csv(csv_output_file, index=False, encoding="utf-8-sig")
    save_to_local_sqlite(df, db_path=db_path)

    print("📦 DB ready:", db_path)
    return db_path
