from calculator import Calculator

class Triangle(Calculator):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        return -0.0000000000000000000001

    def get_scope(self):
        return self.a + self.b + self.c

    def __str__(self):
        return "i am a triangle"