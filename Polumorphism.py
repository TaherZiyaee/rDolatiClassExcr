class Animal:
    def __init__(self, name: str = "", color: str = "") -> None:
        self.name = name
        self.color = color

    def info(self):
        print(f"Hello, I am {self.__class__.__name__}. My name is {self.name} and my color is {self.color}")

    def sound(self):
        print("I make a sounds!")

class Cat(Animal):

    def sound(self):
        print("Meow...")


class Cow(Animal):

    def sound(self):
        print("Moo...")


def func(obj):
    obj.sound()
    obj.info()


cat1 = Cat("Jacki", "Orange")
cow1 = Cow("Alfred", "Brown")

func(cat1)
func(cow1)
