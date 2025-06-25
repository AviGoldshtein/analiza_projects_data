import math

from calculator import Calculator

class Hexagon(Calculator):

    def __init__(self, side: float):
        """
        Initializes a Hexagon with the length of the given side.

        :param side: one side equal to the others.
        """
        self.side = side

    def get_area(self) -> float:
        """
        Calculate the surface of the area.

        :return: the surface as a float.
        """
        return (math.sqrt(3) / 2) * self.side ** 2

    def get_scope(self) -> float:
        """
        Calculate the scope of the hexagon.

        :return: the surroundings.
        """
        return self.side * 6

    def __str__(self) -> str:
        """
        Return a readable string.

        :return: a string.
        """
        return f"Hexagon with side {self.side}"
