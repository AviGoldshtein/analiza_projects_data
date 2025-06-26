from calculator import Calculator

class Rectangle(Calculator):

    def __init__(self, height: float, length: float):
        """
        Initializes a Rectangle with the given height and length.

        :param height: The height of the rectangle.
        :param length: The length (or width) of the rectangle.
        """
        self.height = height
        self.length = length

    def __copy__(self):
        return Rectangle(self.height, self.length)

    def get_area(self) -> float:
        """
        Calculate the area of the rectangle.

        :return: the surface as a float.
        """
        return self.height * self.length

    def get_scope(self) -> float:
        """
        Calculates the surrounding of the rectangle.

        :return: The scope if the rectangle as a float.
        """
        return self.height * 2 + self.length * 2

    def __str__(self) -> str:
        """
        Return a string for readability.

        :return: string of the Rectangle.
        """
        return f"Rectangle with height {self.height} and  length {self.length}"