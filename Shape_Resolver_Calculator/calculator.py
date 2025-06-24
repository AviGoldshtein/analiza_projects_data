from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_scope(self):
        pass