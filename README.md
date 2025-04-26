# Business Insights Dashboard 📊

An interactive dashboard for business performance analysis, powered by **Flask**, **amCharts 5**, and **Pandas**.  
Provides deep insights into **revenue trends**, **market share**, and **regional performance** through dynamic visualizations and KPIs.

---

## 🚀 Features
- 📈 **Market Share Analysis** – Interactive pie charts showing product distribution.
- 💰 **Profit Trend Tracking** – Line charts for analyzing revenue and profit fluctuations.
- 🌍 **Regional Performance Comparison** – Bar charts to compare branch performances.
- 🔢 **Comprehensive KPIs** – Revenue, expenses, customer engagement, and employee metrics.
- 🎨 **User-Friendly Interface** – Built with Flask, HTML5, CSS3, JavaScript, and amCharts 5.

---

## 🛠 Tech Stack
- **Backend:** Flask, SQLAlchemy, SQLite
- **Frontend:** HTML5, CSS3, JavaScript (ES6+), amCharts 5
- **Data Processing:** Pandas

---

## 📂 Project Structure
```plaintext
Business-Insights-Dashboard/
│
├── code/
│   ├── server.py           # Main Flask application
│   ├── static/             # Static assets (CSS, JS, Images)
│   │   ├── css/
│   │   ├── js/
│   ├── templates/          # HTML templates (Jinja2)
│   ├── company.csv         # Sample dataset
│   ├── sample.db           # Sample SQLite database
│
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── LICENSE                 # License file
├── .gitignore              # Git ignored files
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone or Download the Repository
```bash
git clone https://github.com/Moamen-Elsharkawy/Business-Insights-Dashboard.git
cd Business-Insights-Dashboard
```

> **Note:** This repository is **read-only**. Please use it locally — no pull requests or edits will be accepted.

### 2️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv venv
# Activate virtual environment:
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate
```

### 3️⃣ Install Python Dependencies
```bash
pip install -r requirements.txt
```

**Included dependencies** in `requirements.txt`:
```
Flask
Flask-SQLAlchemy
pandas
```

### 4️⃣ Initialize or Use the Database
The repository includes a prebuilt `sample.db` database.  
If you wish to create a new one:

```bash
python
>>> from server import db
>>> db.create_all()
>>> exit()
```

### 5️⃣ Run the Flask Development Server
```bash
python code/server.py
```

Flask will start at:
```
http://127.0.0.1:5000/
```

Open the link in your browser.

---

## 🔒 Repository Policy

- 🛡️ **This repository is read-only.**
- 🚫 No contributions, pull requests, or issues will be accepted.
- 📂 Feel free to **clone, fork, or download** the repository for **personal or business use**.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

# 🚀 Enjoy Using the Business Insights Dashboard!
