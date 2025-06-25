from calculator import Calculator
import math

class Circle(Calculator):

    def __init__(self, radius: float):
        """
        Initializes a Circle with the given radius.

        :param radius: the radius of the circle.
        """
        self.radius = radius


    def __add__(self, other:'Circle') -> float:
        """
        Adds the surface areas of two circles.

        :param other: Another Circle object.
        :return: Sum of the surface areas of both circles.
        """
        return self.get_area() + other.get_area()

    def get_area(self) -> float:
        """
        Calculates the area (surface) of the circle.

        :return: The area of the circle as a float.
        """
        return math.pi * (self.radius ** 2)

    def get_scope(self) -> float:
        """
        Calculates the surrounding of the circle.

        :return: The scope if the circle as a float.
        """
        return 2 * math.pi * self.radius

    def __str__(self) -> str:
        """
        Return a string for readability.

        :return: string of the circle.
        """
        return f"Circle with radius {self.radius}"