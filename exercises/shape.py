class Shape:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.area = None
        self.perimeter = None

    def show(self):
        info = ""
        for key, value in self.__dict__.items():
            info += f"{key} = {value:.2f}\n"
        print(info)

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def __str__(self):
        return self.__class__.__name__

# length, width
class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_perimeter(self):
        self.perimeter = (self.length + self.width) * 2


# length
class Square(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length ** 2

    def calculate_perimeter(self):
        self.perimeter = self.length * 4


def main():
    sh1 = Shape(name="circle", qotr=5)

    # print(sh1.name)
    # print(sh1.__dict__)

    # sh1.show()

    rec1 = Rectangle(length=3.4, width=6.5)
    rec1.calculate_area()
    rec1.calculate_perimeter()
    rec1.show()

    sqr1=Square(length=5)
    sqr1.calculate_perimeter()
    sqr1.calculate_area()
    sqr1.show()

if __name__ == "__main__":
    main()



