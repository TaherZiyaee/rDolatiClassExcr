from  datetime import datetime
class Product:
    def __init__(self,product_name,price,off):
        self.product_name=product_name
        self.price=price
        self.off=off

    def __str__(self):
        return f"Product Name: {self.product_name}\n" \
               f"Price: {self.price}\n" \
               f"Off: {self.off}%"

class Comment:
    website_name="taherlearn.ir"
    def __init__(self,product,author,description):
        self.product=product
        self.author=author
        self.description=description
        self.date=datetime.now()
        self.like_count=0
        self.dislike_count=0

    def show(self):
        print(f"Product: {self.product}\n"
              f"Author: {self.author}\n"
              f"Description: {self.description}\n"
              f"Date: {self.date}\n"
              f"Like: {self.like_count}\n"
              f"Dislike: {self.dislike_count}")

    @classmethod
    def info(cls):
        print(f"Website name: {cls.website_name}")

    # @classmethod
    def censorship(self):
        description:str=self.description
        red_words=("unconscious","stupid","paltry")
        for word in red_words:
            if word in description:
                # print("\t\t The comment was censored!")
                description=description.replace(word,"****")
                self.description=description
                break


def main():
    python_course=Product("Python Expert",2500000,15)
    c1=Comment(python_course,"Taher","You are stupid boy.")
    c1.like_count=40
    c1.dislike_count=9
    c1.info()
    c1.censorship()
    c1.show()

if __name__=="__main__":
    main()

