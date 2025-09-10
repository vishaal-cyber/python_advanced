from abc import ABC, abstractmethod
import math, random

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


# Derived class: Square
class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def draw(self):
        print(f"Drawing a Square with side = {self.side}")

    def area(self) -> float:
        return self.side * self.side

    def perimeter(self) -> float:
        return 4 * self.side


# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self):
        print(f"Drawing a Circle with radius = {self.radius}")

    def area(self) -> float:
        return math.pi * self.radius * self.radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length: float, breadth: float):
        self.length = length
        self.breadth = breadth

    def draw(self):
        print(f"Drawing a Rectangle with length = {self.length}, breadth = {self.breadth}")

    def area(self) -> float:
        return self.length * self.breadth

    def perimeter(self) -> float:
        return 2 * (self.length + self.breadth)

#############################################################################

def Test1():
    shapes: list[Shape] = [
        Square(5),
        Circle(3),
        Rectangle(4, 6)
    ]

    for shape in shapes:
        shape.draw()
        print(f"Area = {shape.area():.2f}")
        print(f"Perimeter = {shape.perimeter():.2f}")
        print("-" * 40)


#----------------------------------------------------------------------------

def Test2():
    
    sh: Shape = None


    for _ in range(5):
        choice = random.choice(["Square", "Circle", "Rectangle"])
        if choice == "Square":
            sh = Square(random.randint(1, 10))
        elif choice == "Circle":
            sh = Circle(random.randint(1, 10))
        else:
            sh = Rectangle(random.randint(1, 10), random.randint(1, 10))

        sh.draw()
        print(f"Area = {sh.area():.2f}")
        print(f"Perimeter = {sh.perimeter():.2f}")



if __name__ == "__main__":
    Test1()
    print("=" * 80)
    Test2()