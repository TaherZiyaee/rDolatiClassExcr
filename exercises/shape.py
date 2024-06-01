class Shape:
    def __init__(self,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)

sh1=Shape(name="circle",qotr=5)

print(sh1.name)
print(sh1.__dict__)