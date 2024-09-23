import math

class Shape:
    def __init__(self, *args):
        self.args = args
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def calculate_area(self):
        prd = 1
        for i in self.args:
            prd = prd * pow(i,2) * math.pi
        return prd
    
    def calculate_perimeter(self):
        prd = 1
        for i in self.args:
            prd = prd* 2 * i * math.pi
        return prd
    
class Rectangle(Shape):
    def calculate_area(self):
        prd = 1
        for i in self.args:
            prd *= i
        return prd
    
    def calculate_perimeter(self):
        sum = 0
        for i in self.args:
            sum += i
        return sum*2


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())