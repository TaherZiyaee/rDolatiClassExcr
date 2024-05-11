class Book:
    def __init__(self,title:str,author:str,year:str)->None:
        self.title=title
        self.author=author
        self.year=year

    def __str__(self):
        return f"Title:\t{self.title}\nAuthor:\t{self.author}\nYear:\t{self.year}"

bk1=Book("Atomic Habits","James Clear","2018")

print(bk1)