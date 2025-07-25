# 🌍 AkashDrishti – Satellite Change Detection & Alert System

> Robust Change Detection, Monitoring, and Alert System on User-Defined AOI Using Multi-Temporal Satellite Imagery  
> 🚀 Built for ISRO Hackathon 2025 | Team: AkashDrishti

---

## 🛰️ Overview

**AkashDrishti** is a web-based geospatial dashboard that allows users to:
- Select any Area of Interest (AOI) on a map
- Specify a date range
- Retrieve satellite imagery (Sentinel-2 or simulated)
- Perform NDVI-based vegetation change detection
- Automatically send alerts if significant changes are detected

Built with **Python + Flask + Leaflet + OpenCV + Firebase**.

---

## 📸 Demo

🔗 **Live Site:** [https://akashdrishti-prototype.onrender.com](https://akashdrishti-prototype.onrender.com)  
📦 **GitHub Repo:** [https://github.com/Manas51240/akashdrishti-prototype](https://github.com/Manas51240/akashdrishti-prototype)

---

## 📍 Features

- ✅ User AOI selection via interactive map (Leaflet)
- ✅ Start/End date input
- ✅ NDVI simulation and comparison logic
- ✅ Automated alerts on detected changes (via email)
- ✅ Real-time visualization dashboard (HTML/CSS/Tailwind-ready)
- ✅ Modular Flask backend with Blueprints

---

## 🧰 Tech Stack

| Layer       | Technology                     |
|------------|----------------------------------|
| Frontend   | HTML, CSS, Leaflet.js            |
| Backend    | Python, Flask                    |
| Image Proc | OpenCV, NumPy                    |
| Auth/Data  | Firebase                         |
| Hosting    | Render.com (Flask App)           |

---

👨‍💻 Authors & Contributors
Team: AkashDrishti – Bharatiya Antariksh Hackathon 2025

👨‍💻 Manas Deshmukh – Python, Flask, Firebase Integration

🧠 Samarth Yete – Database Management, AI Alert System

🎨 Rutuja Jadhav – Frontend Design, UI/UX

🖌️ Shweta Kharat – Graphics & Visual Design

---

## 🔧 Setup Instructions

```bash
git clone https://github.com/Manas51240/akashdrishti-prototype.git
cd akashdrishti-prototype
pip install -r requirements.txt
python app.py
