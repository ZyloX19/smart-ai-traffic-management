# main.py
from vision.vehicle_detector import VehicleDetector

vehicle_detector = VehicleDetector()  # create object

from flask import Flask, jsonify
from flask_cors import CORS

from agents.decision_agent import DecisionAgent
from agents.emergency_agent import EmergencyAgent
from agents.traffic_observer import TrafficObserver

from vision.vehicle_detector import VehicleDetector  # Simulated detector
import random

app = Flask(__name__)
CORS(app)

decision_agent = DecisionAgent()
emergency_agent = EmergencyAgent()
observer = TrafficObserver()
vehicle_detector = VehicleDetector()  # Step 1: simulated vehicle counts

lanes = ["North", "South", "East", "West"]

# Helper function to convert vehicle count to density
def vehicle_count_to_density(count):
    if count <= 5:
        return "Low"
    elif count <= 15:
        return "Medium"
    else:
        return "High"

@app.route("/simulate", methods=["GET"])
def simulate():
    print("\n📡 /simulate API called")

    observer.logs.clear()

    # Emergency check
    if emergency_agent.detect_emergency():
        print("🚨 Emergency detected → Green corridor activated")
        return jsonify({
            "status": "emergency",
            "message": "Emergency vehicle detected. Green corridor activated."
        })

    print("🚦 Normal traffic flow simulation started")

    for lane in lanes:
        density = random.choice(["Low", "Medium", "High"])
        green_time = decision_agent.decide_signal_time(density)

        print(f"➡ Lane: {lane} | Density: {density} | Green Time: {green_time}s")

        observer.record(lane, density, green_time)

    summary = observer.summary()
    print("📊 Traffic Summary:", summary)

    return jsonify({
        "status": "normal",
        "data": summary
    })


@app.route("/")
def home():
    return jsonify({
        "message": "Smart AI Traffic Management API running"
    })

if __name__ == "__main__":
    print("🔥 Starting Flask Server...")
    app.run(host="127.0.0.1", port=5000, debug=True)

