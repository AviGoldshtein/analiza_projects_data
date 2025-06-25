from calculator import Calculator

class Square(Calculator):

    def __init__(self, side):
        """
        Initializes a Square with the given side.

        :param side: The side of the Square.
        """
        self.side = side

    def get_area(self) -> float:
        """
        Calculates the area (surface) of the Square.

        :return: The area of the Square as a float.
        """
        return self.side ** 2

    def get_scope(self) -> float:
        """
        Calculates the surrounding of the Square.

        :return: The scope if the Square as a float.
        """
        return self.side * 4

    def __str__(self) -> str:
        """
        Return a string for readability.

        :return: string of the Square.
        """
        return f"Square with radius {self.side}"