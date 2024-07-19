class NewList(list):
    @property
    def ave(self):
        return sum(self)/len(self)

lst2=NewList((1,2,3,4))
print(lst2)
print(lst2.ave)


