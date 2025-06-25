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