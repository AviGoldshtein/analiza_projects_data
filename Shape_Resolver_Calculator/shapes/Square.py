from calculator import Calculator

class Square(Calculator):

    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_scope(self):
        return self.side * 4

    def __str__(self):
        return "i am a square"