class BankAccount:
    def __init__(self, int_rate, balance): # don't forget to add some default values for these parameters!
	    self.int_rate = int_rate
        self.balance = balance
        self.balance=0
        print("Hello!!  Welcome to the Deposit & Withdrawal Machine.")
    
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount=float(input("Enter amount to be Withdrawn: ")
		if self.balance>=amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Inusfficient balance ")
	
    def display_account_info(self):
        print("\n Net Available Balance=", self.balance)

    def yield_interest(self):
		
accountOne = {".01", "5.00"}
accountTwo = {".25", "2500"}

accountOne.deposit().deposit().deposit().withdrawal().display_user_balance().yield_interest().display_account_info()
accountTwo.deposit().deposit().withdrawal().withdrawal().withdrawal().withdrawal().yield_interest().display_account_info()


