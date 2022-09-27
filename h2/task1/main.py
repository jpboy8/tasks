from bank import BankAccount

b1 = BankAccount()
b2 = BankAccount()

b1.deposit(100)
b1.withdraw(50)
b1.deposit(25)

b2.deposit(1000)
b2.withdraw(500)
b2.deposit(250)

print(b1.balance)
print(b2.balance)