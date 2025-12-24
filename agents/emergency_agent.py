# agents/emergency_agent.py

class EmergencyAgent:
    def detect_emergency(self):
        # Simulated detection (later replace with OpenCV)
        import random
        return random.choice([True, False])

    def override_signal(self):
        return "🚑 EMERGENCY DETECTED → GREEN CORRIDOR ACTIVATED"
