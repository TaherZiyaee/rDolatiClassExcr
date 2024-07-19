class NameField:
    def __set_name__(self, owner, name):
        self.name=name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if 0 < len(value) < 15:
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f"Invalid name {value!r}")

    def __delete__(self, instance):
        print(f"{self.name!r} is deleting...")
        del instance.__dict__[self.name]


class Parent:
    child_name = NameField()
    father_name = NameField()
    mother_name = NameField()

    def __init__(self, child, father, mother):
        self.child_name = child
        self.father_name = father
        self.mother_name = mother


p = Parent("Saman", "Ali", "Mahshid")
print(p.child_name)
print(p.father_name)
print(p.mother_name)
print(p.__dict__)
