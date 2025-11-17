from flask import Flask, jsonify, request
from flask_cors import CORS
from db_loader import load_data
import traceback
import math
import os
from datetime import datetime
from threading import Thread
from app import process_today_data

app = Flask(__name__)
CORS(app)  # Allow React frontend to connect


# --- 🧩 Helper function ---
def sanitize_json(obj):
    """Recursively replace NaN/Infinity with None to make data JSON-safe."""
    if isinstance(obj, list):
        return [sanitize_json(v) for v in obj]
    elif isinstance(obj, dict):
        return {k: sanitize_json(v) for k, v in obj.items()}
    elif isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
        return obj
    else:
        return obj




@app.route("/api/upload", methods=["POST"])
def upload_pdfs():
    try:
        if "files" not in request.files:
            return jsonify({"error": "No files part in the request"}), 400

        files = request.files.getlist("files")
        if not files:
            return jsonify({"error": "No files selected"}), 400

        today = datetime.now().strftime("%d-%m-%Y")
        upload_dir = os.path.join("uploads", today)
        os.makedirs(upload_dir, exist_ok=True)

        saved_files = []

        for file in files:
            if not file.filename.lower().endswith(".pdf"):
                return jsonify({"error": f"{file.filename} is not a PDF file"}), 400

            file_path = os.path.join(upload_dir, file.filename)
            file.save(file_path)
            saved_files.append(file_path)
            print(f"✅ Saved: {file_path}")

        # 🚀 Run processing in background
        def background_task():
            print("⚙️ Background PDF processing started...")
            process_today_data()
            print("🎉 Background PDF processing completed.")

        Thread(target=background_task).start()

        return jsonify({
            "message": "Files uploaded successfully. Processing will continue in background.",
            "saved_files": saved_files
        }), 200

    except Exception as e:
        print("❌ ERROR (upload):", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
@app.route("/api/status", methods=["GET"])
def get_status():
    today = datetime.now().strftime("%d-%m-%Y")
    db_path = f"./output/student_results_{today}.db"

    return jsonify({
        "status": "ready" if os.path.exists(db_path) else "processing"
    })


# --- 📊 Department endpoint ---
@app.route("/api/department", methods=["GET"])
def get_department_data():
    try:
        df = load_data()
        department = request.args.get("department")
        semester = request.args.get("semester")

        filtered = df.copy()

        if department:
            filtered = filtered[filtered["Department"].str.lower() == department.lower()]
        if semester:
            filtered = filtered[filtered["Semester"].astype(str) == str(semester)]

        total_students = len(filtered)
        avg_marks = filtered["Grand_Total_Marks"].mean() if total_students > 0 else 0

        result = {
            "total_students": total_students,
            "avg_marks": round(avg_marks, 2),
            "data": filtered.head(10).to_dict(orient="records")
        }

        # ✅ Sanitize before returning
        safe_result = sanitize_json(result)
        return jsonify(safe_result)

    except Exception as e:
        print("❌ ERROR (department):", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# --- 🧠 Overview endpoint ---
@app.route("/api/overview", methods=["GET"])
def get_overview():
    try:
        df = load_data()
        if isinstance(df, dict) and "error" in df:
            return jsonify(df), 500

        total_students = len(df)

        students_per_department = (
            df.groupby("Department")
            .size()
            .reset_index(name="Total_Students")
            .to_dict(orient="records")
        )

        avg_marks_per_department = (
            df.groupby("Department")["Grand_Total_Marks"]
            .mean()
            .reset_index(name="Average_Marks")
            .to_dict(orient="records")
        )

        result = {
            "total_students": total_students,
            "students_per_department": students_per_department,
            "avg_marks_per_department": avg_marks_per_department
        }

        # ✅ Sanitize before jsonify
        safe_result = sanitize_json(result)
        return jsonify(safe_result)

    except Exception as e:
        print("❌ ERROR (overview):", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# --- 🚀 Run the server ---
if __name__ == "__main__":
    app.run(debug=True, port=5000)
