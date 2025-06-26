from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def get_area(self):
        """
        only for inheritance
        """
        pass

    @abstractmethod
    def get_scope(self):
        """
        only for inheritance
        """
        pass

    # +
    def __add__(self, other):
        return self.get_area() + other.get_area()

    # -
    def __sub__(self, other):
        return self.get_area() - other.get_area()

    # *
    def __mul__(self, other):
        return self.get_area() * other.get_area()

    # /
    def __truediv__(self, other):
        return self.get_area() / other.get_area()

    # //
    def __floordiv__(self, other):
        return self.get_area() // other.get_area()

    # %
    def __mod__(self, other):
        return self.get_area() % other.get_area()





    # <
    def __lt__(self, other) -> bool:
        return self.get_area() < other.get_area()

    # <=
    def __le__(self, other) -> bool:
        return self.get_area() <= other.get_area()

    # ==
    def __eq__(self, other) -> bool:
        return self.get_area() == other.get_area()

    # >
    def __gt__(self, other) -> bool:
        return self.get_area() > other.get_area()

    # >=
    def __ge__(self, other) -> bool:
        return self.get_area() >= other.get_area()

    # bool
    def __bool__(self) -> bool:
        return self.get_area() != 0

