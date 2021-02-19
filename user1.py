

class User:
    def __init__(self, nameOfUser, depositAmount, withdrawalAmount, balance):
        self.name = nameOfUser
        self.depositAmount = depositAmount
        self.withdrawalAmount = withdrawalAmount
        self.balance = balance

    def make_deposit(self):
        print(f"{self.name} makes deposits {self.depositAmount}")
        return self
    
    def make_withdrawal(self):
        print(f"{self.name} makes withdrawal {self.withdrawalAmount}")
        return self
  
    def display_user_balance(self):
        print(f"{self.name} checks balance {self.balance}")
        return self


jaime = User("Jaime", "10", "1", "29")
christian = User("Christian", "10", "5", "10")
shiloh = User("Shiloh", "5", "1", "1")

jaime.make_deposit().make_deposit().make_deposit().make_withdrawal().display_user_balance()
christian.make_deposit()
christian.make_deposit().make_withdrawal().make_withdrawal().display_user_balance()
shiloh.make_deposit().make_withdrawal().make_withdrawal().make_withdrawal().display_user_balance()
