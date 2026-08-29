from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Anomaly Detector API")

# Allow dashboard.html to talk to server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store last 100 readings here
data_store = []

class DataPoint(BaseModel):
    y: float
    anomaly: bool

@app.get("/")
def home():
    return {"message": "Anomaly Detector API is running. Go to /dashboard"}

@app.post("/data")
def receive_data(point: DataPoint):
    """test_anomaly.py sends data here"""
    data_store.append(point.dict())
    if len(data_store) > 100:  # keep only last 100
        data_store.pop(0)
    return {"status": "ok", "received": point.dict()}

@app.get("/latest")
def get_latest():
    """dashboard.html asks for newest data here"""
    if len(data_store) == 0:
        return {"y": 50, "anomaly": False} # default while waiting
    return data_store[-1]  # send the newest point

@app.get("/dashboard")
def serve_dashboard():
    """open this in browser"""
    return FileResponse("dashboard.html")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)