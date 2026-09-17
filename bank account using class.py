"""
Problem Statement:  
Design a banking system using three classes:

BankAccount

Attributes: account_number, balance

Methods: deposit(amount), withdraw(amount)

SavingAccount (inherits from BankAccount)

Attribute: interest_rate

Method: add_interest() → adds interest to the balance

FixedDepositAccount (inherits from SavingAccount)

Attributes: fd_amount, fd_period (in years)

Method: maturity_amount() → calculates maturity using simple interest formula:

Task:

Create an object of FixedDepositAccount.

Demonstrate depositing money, adding interest, and calculating maturity amount.
"""

class BankAccount:
    
    def __init__(self , account_number , balance = 0 ):
        self.account_number = account_number 
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount 
        print(f"Deposited Amount {amount} . Account Balance {self.balance}")
        
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount 
            print(f"Account Balance {self.balance}")
        else:
            print('Insufficient Balance')
    
class SavingAccount(BankAccount):
    
    def __init__(self , account_number , balance , interest):
        super().__init__(account_number ,balance)
        self.interest = interest 
    def add_interest(self):
        self.balance += (self.balance * self.interest )
        print(f"Account Balance {self.balance}")
    
class FixedDepositAccount(SavingAccount):
    def __init__(self,account_number , balance , interest , fd_amount , fd_period):
        super().__init__(account_number ,balance , interest)
        self.fd_amount = fd_amount 
        self.fd_period = fd_period
    def maturity_amount(self):
        maturity = self.fd_amount + (self.fd_amount * self.interest * self.fd_period)
        print('Maturity Amount',maturity)
        
user = FixedDepositAccount(101,1000,0.07 , 10000,3)
user.deposit(10000)
user.withdraw(500)
user.add_interest()
user.maturity_amount()
