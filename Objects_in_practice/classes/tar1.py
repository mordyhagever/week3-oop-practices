

class Player:
    def __init__(self, name, points=0):
        self.name = name
        self.points = points

    def add_points(self, amount):
        self.points += amount

    def get_points(self):
        return self.points

    def __str__(self):
        return f"{self.name}: {self.get_points()}"



