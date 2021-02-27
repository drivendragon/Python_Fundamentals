class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = 0
    def make_deposit(self, amount):
        self.account += amount
        return self
    def make_withdrawal(self, amount):
        self.account -= amount
        return self
    def display_user_balance(self):
        print(f"My account balance is: {self.account}")
        return self

class User1:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account
        return self
    def make_withdrawal(self, amount):
        self.account
        return self
    def display_user_balance(self):
        print(f"My account balance is: {self.account}")
        return self


user1 = User("dragon", "drivendragon@hotmail.com")
user2 = User("jaime", "jaime@gmail.com")
user1.make_deposit(6).make_withdrawal(2).display_user_balance()
user2.make_deposit(500).make_deposit(500).make_withdrawal(250).display_user_balance()