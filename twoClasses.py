class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self.account_balance
    def display_user_balance(self):
        print(f"My account balance is: {self.account_balance}")
        return self.account_balance

user1 = User("dragon", "drivendragon@hotmail.com")
user2 = User("jaime", "jaime@gmail.com")

print(user1.make_deposit(500))
print(user2.make_deposit(100))

print(user1.make_withdrawal(100))
print(user2.make_withdrawal(10))

print(user1.display_user_balance())
print(user2.display_user_balance())