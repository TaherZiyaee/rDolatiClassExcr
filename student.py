class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.__age = age
        self.score = None
        if 6 < age > 100:
            print(f"You enter {self.__age} for age!. It's not valid!")
            self.__age = None

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.__age}"


st = Student("Taher Ziayee", 398)

print(st)
