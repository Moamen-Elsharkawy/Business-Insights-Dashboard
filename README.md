# Business-Insights-Dashboard
An interactive amCharts 5 and Flask-based dashboard for business performance analysis. It utilizes Pandas for data processing, SQLite for storage, and JavaScript for dynamic visualizations. The dashboard provides insights into revenue trends, market share, and regional performance through interactive charts and KPIs, aiding data-driven decisions.
 # Business Insights Dashboard 📊
 
## 🚀 Features
- 📈 **Market Share Analysis** – Visualizes product distribution with interactive pie charts.
- 💰 **Profit Trend Tracking** – Line charts to analyze revenue and profit fluctuations.
- 🌍 **Regional Performance Comparison** – Bar charts to compare branch performance.
- 🔢 **Comprehensive KPIs** – Revenue, expenses, customer engagement, and employee data.
- 🎨 **User-Friendly Interface** – Built with Flask, HTML, CSS, and JavaScript.

## 🛠 Tech Stack
- **Backend:** Flask, SQLAlchemy, SQLite
- **Data Processing:** Pandas
- **Frontend:** HTML, CSS, JavaScript, amCharts 5

## 📂 Project Structure
```
Business-Insights-Dashboard/
│── code/
│   ├── server.py   # Main Flask application
│   ├── static/     # Static assets (CSS, JS, images)
│   ├── templates/  # HTML templates for UI
│   ├── company.csv # Sample dataset
│   ├── sample.db   # SQLite database file
│── README.md
│── requirements.txt  # Dependencies
```

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Business-Insights-Dashboard.git
cd Business-Insights-Dashboard
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Flask Server
```bash
python server.py
```
### 4️⃣ Access the Dashboard
Open your browser and go to:
```
http://127.0.0.1:5000/
```
