import random

class VehicleDetector:
    def __init__(self, video_path=None):
        # Video path is optional for simulation
        self.lanes = ["North", "South", "East", "West"]

    def detect_vehicles(self):
        """
        Simulate vehicle counts per lane.
        Returns dict: {lane_name: vehicle_count}
        """
        vehicle_counts = {}
        for lane in self.lanes:
            # Simulate 0-20 vehicles per lane
            vehicle_counts[lane] = random.randint(0, 20)
        return vehicle_counts


# Optional helper function (can also be in main.py)
def vehicle_count_to_density(count):
    if count <= 5:
        return "Low"
    elif count <= 15:
        return "Medium"
    else:
        return "High"
