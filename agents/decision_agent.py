
class DecisionAgent:
    def decide_signal_time(self, density):
        if density == "High":
            return 60
        elif density == "Medium":
            return 40
        else:
            return 25
