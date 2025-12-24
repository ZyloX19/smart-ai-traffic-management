
class TrafficObserver:
    def __init__(self):
        self.logs = []

    def record(self, lane, density, green_time):
        self.logs.append({
            "lane": lane,
            "density": density,
            "green_time": green_time
        })

    def summary(self):
        return self.logs
