from pprint import pprint
from datetime import datetime

seller_time_format = "%Y/%m/%d - %H:%M:%S %p"

class UserList(list):
    def search(self,username:str)->list:
        matching_list=[]
        for user in self:
            if username in user.username:
                matching_list.append(user)
        return matching_list

    def append(self, obj) -> None:
        if not isinstance(obj,User):
            raise TypeError("This is only accepts User.")
        else:
            return super().append(obj)

class User:
    # all_users = list()
    all_users = UserList()

    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        self.password = password
        User.all_users.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.username!r}, {self.email!r}, {self.password!r})"

    def __str__(self):
        return f"From {self.__class__.__name__!r} class: {self.username}"


class Order:
    def __init__(self, product_type: str, number: float):
        if number > 1:
            product_type += 's'

        self.selling_date = datetime.today().strftime(seller_time_format)
        self.product_name = ""
        self.product_type = product_type
        self.number = number


class Seller(User):
    def order(self, order: "Order") -> None:
        print(f"\nHi {self.username},\n\tfrom your products, {order.number} {order.product_type}"
              f" was sold at {order.selling_date}.")

class Buyer(User):
    def __init__(self,username: str, email: str, password: str,phone:str):
        super().__init__(username,email,password)
        self.phone=phone

    def __repr__(self):
        return f"{self.__class__.__name__}({self.username!r}, {self.email!r}, {self.password!r}, {self.phone!r})"

def main():
    usr1 = User("Taher", "tata@gmail.com", "1234")
    print(usr1)

    usr2=User("Saman","sam@gmail.com","87fd6")

    sl1 = Seller("Noyan", "nono@yahoo.com", "76125")
    print(sl1)

    print("\nAll users:")
    pprint(User.all_users)

    ord1 = Order("book", 1)

    sl1.order(ord1)

    print("\nSearch user:")
    pprint(User.all_users.search("an"))

    print()
    buy1=Buyer("Ali","ali@yahoo.com","87fsd6","091278")
    print(repr(buy1))

    # User.all_users.append(4)

    print("\nAll users:")
    pprint(User.all_users)




if __name__ == "__main__":
    main()
