from datetime import datetime

seller_time_format = "%Y/%m/%d - %H:%M:%S %p"


class User:
    all_users = list()

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
    def order(self, order: "Order"):
        print(f"Hi {self.username},\n\tfrom your products, {order.number} {order.product_type}"
              f" was sold at {order.selling_date}.")


def main():
    usr1 = User("Taher", "tata@gmail.com", "1234")
    print(usr1)

    sl1 = Seller("Noyan", "nono@yahoo.com", "76125")
    print(sl1)

    ord1 = Order("book", 1)

    sl1.order(ord1)


if __name__ == "__main__":
    main()
