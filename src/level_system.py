class LevelSystem:
    def __init__(self, base=50, max_level=10):
        self.level = 1
        self.base = base
        self.max_level = max_level

    def update(self, score):
        while self.level < self.max_level and score >= self.required_points(self.level + 1):
            self.level += 1

    def required_points(self, level):
        return sum(self.base * i for i in range(1, level))

    def get_level(self):
        return self.level

    def get_progress(self, score):
        current = self.required_points(self.level)
        next_level = self.required_points(self.level + 1)
        if next_level == current:
            return 1.0
        return min((score - current) / (next_level - current), 1.0)