def dec(func):
    def inner():
        print("**********")
        func()
        print("**********")
    return inner

@dec
def func():
    print("Taher")



func()