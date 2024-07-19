class C:
    def __enter__(self):
        print("Start!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print("End!")
        return True

with C() as c:
    print('-'*20)
    print(17)
    print(10/0)
    print("TAHER")
    print('-'*20)