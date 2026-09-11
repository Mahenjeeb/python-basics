from math import pi
class Square:
    # non static method instance should be created
    # 'self' can be accessed
    def area(self, length):
        print(f"Area Of Square{length * length}")

class Circle:
    # static method no 'self' required.
    # directly access it using calss name
    @staticmethod
    def area(radius):
        print(f"Area of Circle {pi * radius * radius}")
    @staticmethod
    def perimeter(radius):
        print(f"Perimeter of Circle {2 * pi * radius}")

sqArea = Square()
sqArea.area(2)
Circle.area(4)
Circle.perimeter(4)