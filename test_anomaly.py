import requests
import random
import time

URL = "http://127.0.0.1:8000/data"  # your server endpoint
TOTAL_READINGS = 100  # <-- only 100 readings
DELAY_SECONDS = 1     # 1 reading per second

print(f"Starting... will send {TOTAL_READINGS} readings and then stop")

for i in range(1, TOTAL_READINGS + 1):
    # Generate fake sensor value
    value = random.gauss(50, 10)  # normal around 50
    
    # Make 10% of them big spikes = anomalies
    is_anomaly = False
    if random.random() < 0.1:  # 10% chance
        value = random.gauss(120, 15) # big spike
        is_anomaly = True

    payload = {
        "y": round(value, 2),
        "anomaly": is_anomaly
    }

    try:
        res = requests.post(URL, json=payload)
        print(f"[{i}/{TOTAL_READINGS}] Sent: y={payload['y']}, anomaly={payload['anomaly']} | Status: {res.status_code}")
    except Exception as e:
        print(f"Error sending: {e}")

    time.sleep(DELAY_SECONDS)

print("\n✅ Done! Sent all 100 readings. Stopping now.")