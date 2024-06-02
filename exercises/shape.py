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


class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_perimeter(self):
        self.perimeter = (self.length + self.width) * 2


sh1 = Shape(name="circle", qotr=5)

# print(sh1.name)
# print(sh1.__dict__)

# sh1.show()

rec1 = Rectangle(length=3.4, width=6.5)
rec1.calculate_area()
rec1.calculate_perimeter()
rec1.show()
