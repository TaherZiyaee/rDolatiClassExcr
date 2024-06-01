class Vehicle:
    def __init__(self,number_of_wheel:int):
        self.number_of_wheel=number_of_wheel
        self.fuel_type="Something"
    def info(self):
        print(f"It's a {self.__class__.__name__}.\nIt has {self.number_of_wheel} wheels.\nMy fuel type is {self.fuel_type}")


class Car(Vehicle):
    def __init__(self,doors_number,**kwargs):
        super().__init__(**kwargs)
        self.doors_number=doors_number
        self.sun_roof = False
        self.fuel_type="Petrol"


class Bicycle(Vehicle):
    pass

class Airplane(Vehicle):
    pass

class Lamborghini(Car):
    pass

class Benz(Car):
    def __init__(self,model:str,**kwargs):
        super().__init__(**kwargs)
        self.model=model
    def info(self):
        print(
            f"It's a {self.__class__.__name__} model {self.model}.\nIt has {self.number_of_wheel} wheels.\nMy fuel type is {self.fuel_type}."
            f"\nNumber of doors are {self.doors_number}.")

benz1 = Benz("C200",number_of_wheel=4,doors_number=4)
benz1.info()