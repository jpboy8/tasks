class BankAccount:

    def __init__(self, balance: int = 0):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if type(value) not in (int, float) or value < 0:
            raise ValueError("balance must be integer or float and positive!")
        self.__balance = value

    def deposit(self, amount): 
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
