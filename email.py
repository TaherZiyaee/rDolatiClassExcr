class Email:
    def __init__(self, sender: str, receiver: str) -> None:
        self.sender = sender
        self.receiver = receiver
        self.subject = ""
        self.body = ""

    def __str__(self):
        print('-' * 40)
        return f"\nFrom:\n\t{self.sender}\nTo:\n\t{self.receiver}\nSubject:\n\t{self.subject}\nContext:\n\t{self.body}"

    def send_email(self, subject):
        self.subject = subject
        self.body = input("Please enter context of Email: ")
        print(self)


eml1 = Email("taher@gmail.com", "noyan@gmail.com")
eml1.send_email("Hello")
