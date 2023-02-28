from typing import List
from math import sqrt


class Polygon:
    """
    The Polygon class has a constructor that takes a list of floats representing the lengths of its sides, and a method display_sides() that returns the sides.
    """

    def __init__(self, sides: List[float]) -> None:
        self.sides = sides

    def display_sides(self) -> List[float]:
        return self.sides


class Triangle(Polygon):
    """
    The Triangle class inherits from Polygon and implements a find_area() method to calculate the area of the triangle using Heron's formula.
    """

    def find_area(self):
        a, b, c = self.sides[0], self.sides[1], self.sides[2]

        if a < 0 or b < 0 or c < 0:
            return print("one of the sides has a negative length.")
        elif a > b + c or b > a + c or c > a + b:
            return print("one of the sides has a length greater than or equal to the sum of the lengths of the other two sides (forming a degenerate triangle).")
        else:
            s = (a + b + c) / 2
            area = sqrt(s * (s-a) * (s-b) * (s-c))

            return area


test_1 = Triangle([2, 3, 4])
test_2 = Triangle([2, 3, 2])
test_3 = Triangle([2, 2, 2])
test_4 = Triangle([2, 2, 20])
test_5 = Triangle([2, 2, -2])

print(test_1.find_area())
print(test_2.find_area())
print(test_3.find_area())
print(test_4.find_area())
print(test_5.find_area())
