import math

from calculator import Calculator

class Hexagon(Calculator):

    def __init__(self, side):
        self.side = side

    def get_area(self):
        return (math.sqrt(3) / 2) * self.side ** 2

    def get_scope(self):
        return self.side * 6

    def __str__(self):
        return "i am a hexagon"
