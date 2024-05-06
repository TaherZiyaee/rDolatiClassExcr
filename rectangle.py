class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return (self.width + self.height) * 2

    def __repr__(self) -> str:
        return f"Width = {self.width}, Height = {self.height}\n" \
               f"Area = {self.area()}\nPerimeter = {self.perimeter()}"


rec1 = Rectangle(2, 4)
print(rec1)
