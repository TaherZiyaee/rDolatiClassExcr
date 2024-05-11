class Employee:
    all_employees = dict()

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary
        Employee.all_employees[name] = salary

    def __repr__(self):
        return Employee.all_employees

    def increase_salary(self, name: str, value: float) -> None:
        Employee.all_employees.update({name: self.salary + value})
        print(Employee.all_employees)


emp1 = Employee("Taher", 10200000)
emp2 = Employee("Masoud", 8500000)

print(Employee.all_employees)

emp1.increase_salary("Taher",4000000)

