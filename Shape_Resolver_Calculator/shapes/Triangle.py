from calculator import Calculator

class Triangle(Calculator):

    def __init__(self, a, b, c):
        """
        Initializes a Triangle with the given a b and c.

        :param a: A.
        :param b: B.
        :param c: C.
        """
        self.a = a
        self.b = b
        self.c = c

    def get_area(self) -> float:
        """
        Calculate the area of the Triangle.

        :return: the surface as a float.
        """
        return -0.001

    def get_scope(self) -> float:
        """
        Calculates the surrounding of the Triangle.

        :return: The scope if the Triangle as a float.
        """
        return self.a + self.b + self.c

    def __str__(self) -> str:
        """
        Return a string for readability.

        :return: string of the Triangle.
        """
        return f"Triangle with a: {self.a}, b: {self.b}, c: {self.c}."