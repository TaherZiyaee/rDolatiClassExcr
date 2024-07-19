class NewObj:
    def __init__(self):
        self.items=[1,2,3,4]

    def __next__(self):
        return 2

n1=NewObj()
print(next(n1))