# simulation/traffic_simulator.py

import random
import time
from agents.decision_agent import DecisionAgent
from agents.emergency_agent import EmergencyAgent
from agents.traffic_observer import TrafficObserver

def run_simulation():
    print("🚦 Smart Traffic Simulation Started")

    decision_agent = DecisionAgent()
    emergency_agent = EmergencyAgent()
    observer = TrafficObserver()

    lanes = ["North", "South", "East", "West"]

    for i in range(5):
        print(f"\n⏱️ Cycle {i + 1}")

        if emergency_agent.detect_emergency():
            print(emergency_agent.override_signal())
            time.sleep(1)
            continue

        for lane in lanes:
            density = random.choice(["Low", "Medium", "High"])
            green_time = decision_agent.decide_signal_time(density)

            observer.record(lane, density, green_time)

            print(
                f"Lane {lane} | Density: {density} | "
                f"Green Signal: {green_time} sec"
            )

        time.sleep(1)

    print("\n📊 Traffic Analytics Summary")
    for record in observer.summary():
        print(record)

    print("\n✅ Smart Traffic Simulation Ended")


if __name__ == "__main__":
    run_simulation()
