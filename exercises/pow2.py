class PowTwo:
    def __init__(self,max_pow):
        self.n=0
        self.max_pow=max_pow

    def __iter__(self):
        return self

    def __next__(self):
        if self.n<=self.max_pow:
            result=self.n**2
            self.n+=1
            return  result
        else:
            raise StopIteration

n=PowTwo(5)
# next(n)
# next(n)
for i in n:
    print(i)