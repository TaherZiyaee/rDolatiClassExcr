class Student:

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.__age = age
        self.scores = list()
        if 6 < age > 100:
            print(f"You enter {self.__age} for age!. It's not valid!")
            self.__age = None

    def add_score(self):
        self.scores = list(map(float, input("Please enter list of marks: ").split()))

    def average(self):
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f"Name:\t\t{self.name}\nAge:\t\t{self.__age}\nAll marks:\t{self.scores}\nAverage:\t{self.average():.2f}"


st = Student("Taher Ziayee", 39)
st.add_score()
print(st)
