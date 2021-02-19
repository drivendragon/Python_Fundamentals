

class User:
    def __init__(self, nameOfUser, depositAmount, withdrawalAmount, balance):
        self.name = nameOfUser
        self.depositAmount = depositAmount
        self.withdrawalAmount = withdrawalAmount
        self.balance = balance

    def make_deposits(self):
        print(f"{self.name} makes deposits {self.depositAmount}")
    
    def make_withdrawal(self):
        print(f"{self.name} makes withdrawal {self.withdrawalAmount}")
  
    def display_user_balance(self):
        print(f"{self.name} checks balance {self.balance}")


jaime = User("Jaime", "10", "1", "29")
christian = User("Christian", "10", "5", "10")
shiloh = User("Shiloh", "5", "1", "1")


jaime.make_deposits()
jaime.make_deposits()
jaime.make_deposits()
jaime.make_withdrawal()
jaime.display_user_balance()
christian.make_deposits()
christian.make_deposits()
christian.make_withdrawal()
christian.make_withdrawal()
christian.display_user_balance()
shiloh.make_deposits()
shiloh.make_withdrawal()
shiloh.make_withdrawal()
shiloh.make_withdrawal()
shiloh.display_user_balance()
