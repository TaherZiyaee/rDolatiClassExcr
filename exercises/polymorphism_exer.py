class Vehicle:
    def __init__(self,number_of_wheel:int):
        self.number_of_wheel=number_of_wheel
        self.fuel_type="Something"
    def info(self):
        print(f"It's a {self.__class__.__name__}.\nIt has {self.number_of_wheel} wheels.\nMy fuel type is {self.fuel_type}")


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.fuel_type="Petrol"

class Bicycle(Vehicle):
    pass

class Airplane(Vehicle):
    pass

class Lamborghini(Car):
    pass

class Benz(Car):
    def __init__(self):
        super().__init__()

benz1 = Benz(4)
benz1.info()