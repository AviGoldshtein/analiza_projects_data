from calculator import Calculator

class Rectangle(Calculator):

    def __init__(self, hight, length):
        self.hight = hight
        self.length = length

    def get_area(self):
        return self.hight * self.length

    def get_scope(self):
        return self.hight * 2 + self.length * 2

    def __str__(self):
        return "i am a rectangle"