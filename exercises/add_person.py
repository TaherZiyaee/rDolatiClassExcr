class Person:
    def __init__(self, first_name: str, last_name: str, age: float, national_code: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.national_code = national_code

    def __str__(self):
        return f"Full Name: {self.first_name} {self.last_name}"

    def __add__(self, other):
        return self.age + other.age


p1 = Person("Taher", "Ziaei", 38, "823765431")
p2 = Person("Noyan", "Ziaei", 7, "9182376327")

print(f"Sum of ages: {p1 + p2}")
