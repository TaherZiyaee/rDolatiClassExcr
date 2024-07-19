def dash(func):
    def inner(*x,**y):
        print("------")
        func(*x,**y)
        print("------")
    return inner

def star(func):
    def inner(*x,**y):
        print("******")
        # func(*x,**y)
        print("******")
    return inner

@dash
@star
def func():
    print("Taher")

func()