class Car:
    def __init__(self) -> None:
        self.brand: str = ""
        self.model: str = ""
        self.year: str = ""

    def entry(self) -> None:
        self.brand = input("Please enter brand car: ")
        self.model = input("Please enter model car: ")
        self.year = input("Please enter year car: ")

    def __str__(self) -> str:
        return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}"


car1 = Car()
car1.entry()
print(car1)
