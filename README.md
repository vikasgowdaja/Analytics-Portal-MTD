# 🧠 Analytics Portal (MTD)

A full-stack analytics portal designed to manage and visualize MTD (Month-to-Date) reports using **React (Vite)** on the frontend, **Flask (Python)** on the backend, and **Supabase** for authentication and storage.
## ⚙️ Prerequisites

Before running the project, make sure you have:

* **Python 3.10+**
* **Node.js 18+** (with npm or bun)
* **MySQL** (optional, if using database integration)
* **Supabase** account and project setup

---

## 🚀 Setup Instructions

### 🐍 Backend (Flask)

1. **Navigate to the server directory**

   ```bash
   cd server
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   # or: source .venv/bin/activate  # Mac/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Or install without versions (if required):

   ```bash
   pip install flask flask-cors mysql-connector-python numpy pandas pdfminer.six pdfplumber pillow blinker cffi charset-normalizer click colorama cryptography itsdangerous jinja2 markupsafe pypdfium2 python-dateutil pytz six tzdata werkzeug
   ```

4. **Run the backend**

   ```bash
   python app.py
   ```

   By default, Flask will run on [http://localhost:8000](http://localhost:8000)

---

### ⚛️ Frontend (React + Vite)

1. **Navigate back to the client root**

   ```bash
   cd ..
   ```

2. **Install frontend dependencies**

   ```bash
   npm install
   ```

3. **Start the development server**

   ```bash
   npm run dev
   ```

   The app will be available at [http://localhost:5173](http://localhost:5173)

---

## 🔐 Environment Configuration

Create a `.env` file in the **root directory** (or copy from `.env.example` if available):

```bash
# ============================================
# 🌍 SUPABASE CONFIGURATION
# ============================================
VITE_SUPABASE_PROJECT_ID="your-supabase-project-id"
VITE_SUPABASE_PUBLISHABLE_KEY="your-anon-public-key"
VITE_SUPABASE_URL="https://your-project-id.supabase.co"

# ============================================
# ⚙️ BACKEND CONFIGURATION
# ============================================
SUPABASE_URL="https://your-project-id.supabase.co"
SUPABASE_SERVICE_ROLE_KEY="your-service-role-key"

# ============================================
# 🗄️ DATABASE CONFIGURATION (optional)
# ============================================
DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD=""
DB_NAME="test_db"

# ============================================
# 🧠 APP SETTINGS
# ============================================
APP_ENV="development"
DEBUG=True
PORT=8000
```

---

## 🧩 Tech Stack

| Layer         | Technology                 |
| ------------- | -------------------------- |
| Frontend      | React (Vite) + TailwindCSS |
| Backend       | Flask (Python)             |
| Database      | MySQL / SQLite             |
| Cloud Backend | Supabase                   |
| File Parsing  | PDFMiner + pdfplumber      |
| Visualization | React + Custom Charts      |

---

## 🧰 Troubleshooting

* **If backend doesn’t start:**

  * Check if the virtual environment is activated.
  * Ensure required packages are installed.
  * Check `.env` configuration.

* **If frontend doesn’t load:**

  * Verify `VITE_SUPABASE_*` variables are correct.
  * Ensure the backend (`http://localhost:8000`) is running.

* **If MySQL connection fails:**

  * Check `DB_HOST`, `DB_USER`, and `DB_PASSWORD` in `.env`.
  * Confirm MySQL service is running locally.

---

## 👨‍💻 Development Notes

* All processed files are stored under `server/output/`.
* Uploaded PDFs should go into `server/uploads/`.
* Use `db_loader.py` to migrate or import MySQL/SQLite data.
* Frontend communicates with backend via `/api` routes proxied in Vite config.

---

## 🔗 Repository

**GitHub Repo:** [Analytics-Portal-MTD](https://github.com/vikasgowdaja/Analytics-Portal-MTD.git)

---

## 🤝 Contribution

If you’re setting up locally, please confirm once your environment is running fine.
If you face any errors (backend, React, or Supabase setup), reach out to **Vikas** for help.
