class BankAccount:

    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, amount): 
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
