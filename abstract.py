from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

    def area(self):
        return 3.14159 * self.radius * self.radius

obj = Square(7)
obj2=Circle(7)
print(obj.area())
print(obj.perimeter())
print(obj2.area())
print(obj2.perimeter())