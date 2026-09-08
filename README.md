Real-Time Anomaly Detection Dashboard

A real-time anomaly detection dashboard built with FastAPI.
test_anomaly.py` sends 100 random data points to the server. 
dashboard.html` shows them live. Red dots = Anomaly, Blue = Normal.

 Tech Stack
- Python 3.12
- FastAPI + Uvicorn
- HTML5 Canvas + JavaScript

 Installation
powershell
pip install fastapi uvicorn pydantic

How to Run
Open 2 PowerShell/CMD windows

Window 1: Start the API Serverpowershelluvicorn app:app --host 127.0.0.1 --port 8000

Window 2: Start the Data Senderpowershellpy test_anomaly.py

Open Dashboard:http://127.0.0.1:8000/dashboard

 API Endpoints

**GET /** 
Health check. 
Example: {"message": "Anomaly Detector API is running"}

**POST /data** 
Receives a data point from test_anomaly.py
Example: {"x": 1, "y": 45.2, "anomaly": false}

**GET /latest** 
Returns the newest data point. Used by dashboard
Example: {"x": 5, "y": 82.1, "anomaly": true}

**GET /history** 
Returns last 100 data points for the graph

**GET /dashboard** 
Serves the live HTML dashboard page

