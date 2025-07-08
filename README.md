# 🛰️ AkashDrishti – Satellite-Based Change Detection Prototype

**AkashDrishti** is a robust change detection, monitoring, and alert system using multi-temporal satellite imagery. Built for the **ISRO Bharatiya Antariksh Hackathon 2025**, the prototype allows users to select an Area of Interest (AOI), analyze NDVI-based vegetation change, and visualize results interactively.

---

## 🔧 Features

- 🌍 **AOI Selection via Interactive Map (Leaflet.js)**
- 🧭 **Manual Latitude/Longitude Input**
- 🗓️ **Date Range Selection**
- 🌱 **Simulated NDVI Change Detection**
- 📊 **Results Visualization on Dashboard**
- ⚙️ Built using **Flask + Leaflet + Tailwind CSS**

---

## 📁 Folder Structure

akashdrishti/
├── app/
│ ├── init.py
│ ├── routes/
│ │ └── main.py
│ ├── static/
│ │ ├── css/
│ │ ├── js/
│ │ └── images/
│ ├── templates/
│ │ ├── index.html
│ │ ├── home.html
│ │ ├── aoi.html
│ │ ├── aoi_map.html
│ │ └── results.html
│ └── utils/
│ └── image_analysis.py
├── config.py
├── run.py
├── requirement.txt
└── README.md

yaml
Copy code

---

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Manas51240/akashdrishti-prototype.git
   cd akashdrishti-prototype
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirement.txt
Run the Flask app:

bash
Copy code
python run.py
Open your browser and visit:

cpp
Copy code
http://127.0.0.1:5000
🧠 Future Enhancements
📬 Add Email Notifications on change detection

🛰️ Integrate Real Satellite Imagery (e.g., Sentinel-2 API)

🤖 Add AI-based classifier for Land Cover/Disaster Detection

🗄️ Store user history and AOI data with authentication

📈 Add time-series NDVI graph visualization

🛠️ Tech Stack
🐍 Python Flask – Backend

🗺️ Leaflet.js – AOI Map Drawing

🌐 OpenStreetMap – Map Tiles

🎨 Tailwind CSS – UI Styling

💼 Submission Info
👨‍💻 Developed by: Manas Deshmukh & Team

🛰️ Built for: ISRO Bharatiya Antariksh Hackathon 2025

🔗 GitHub Repository: https://github.com/Manas51240/akashdrishti-prototype