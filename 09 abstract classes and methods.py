# Abstract classes and methods
from abc import abstractmethod,ABC
# Abstract class: Shape for rectangle to inherit

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self,length : float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def main():
    rectangle = Rectangle(3,4)

    print(f"Rectangle area: {rectangle.area()}")
if __name__ == '__main__':
    main()