from calculator import Calculator
import math

class Circle(Calculator):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_scope(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return "i am a circle"