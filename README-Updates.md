# Analytics Portal (MTD)

A portal for analytics and monthly tracking (MTD) built with:

- 🐍 **Python / Flask** backend
- 🌐 **Vite + JavaScript/TypeScript** frontend
- 🗄️ Optional **MySQL** database
- ☁️ **Supabase** integration (for auth / storage as configured)

Repository URL:  
https://github.com/vikasgowdaja/Analytics-Portal-MTD

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/vikasgowdaja/Analytics-Portal-MTD.git
cd Analytics-Portal-MTD
```

---

## 📦 Backend Setup (Flask)

From the project root:

```bash
cd server
```

### 1. Create and Activate Virtual Environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac / Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

Using `requirements.txt` (recommended):

```bash
pip install -r requirements.txt
```

Or, install manually (without pinned versions):

```bash
pip install flask flask-cors mysql-connector-python numpy pandas pdfminer.six pdfplumber pillow blinker cffi charset-normalizer click colorama cryptography itsdangerous jinja2 markupsafe pypdfium2 python-dateutil pytz six tzdata werkzeug
```

### 3. Run the Backend Server
> This command is for Data Processing — your `app.py` entry file is different.

```bash
python app.py
```

> Update this command if your `server.py`/entry file is different.

```bash
python server.py
```
Configure db.py File
```env
# ============================================
# 🗄 DATABASE CONFIGURATION (optional)
# ============================================
DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD=""
DB_NAME="test_db"
```

By default, Flask usually runs at:

- http://127.0.0.1:5000  
- http://localhost:5000

---

## ⚙️ Environment Configuration

Create a `.env` file in the **project root** (same level as `package.json`) with the following template:

```env
# ============================================
# 🌍 SUPABASE CONFIGURATION
# ============================================
VITE_SUPABASE_PROJECT_ID="your-supabase-project-id"
VITE_SUPABASE_PUBLISHABLE_KEY="your-anon-public-key"
VITE_SUPABASE_URL="https://your-project-id.supabase.co"

```

> Make sure not to commit real secrets to GitHub. Add `.env` to your `.gitignore`.

---

## 💻 Frontend Setup (Vite)

From the **project root**:

```bash
npm install
npm run dev
```

Default frontend URL:

- http://localhost:5173

Ensure the API URLs (e.g., `http://localhost:5000`) are correctly configured.

---

## 🌱 Basic Git Workflow (For Team Members)

```bash
git status
git add .
git commit -m "Meaningful message"
git push
```

For first push on a new branch:

```bash
git push -u origin <branch-name>
```

---

## 🛠 Troubleshooting

- **Virtualenv not activating (Windows)** — Use Command Prompt or PowerShell.
- **Module not found** — Verify venv is active and dependencies installed.
- **Port already in use** — Stop previous instance or change port.

---

## 👥 Contact

Owner / Maintainer: **Vikas Gowda J A**  
GitHub: [@vikasgowdaja](https://github.com/vikasgowdaja)
