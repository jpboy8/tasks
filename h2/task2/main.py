from money import Money

from wallet import Wallet


m1 = Money('m1', 100, 'USD', 5)
m2 = Money('m2', 200, 'USD', 1)
m3 = Money('m3', 300, 'USD', 1)

w1 = Wallet([m3, m2])
print(f'Initialization:\n{w1}')

# get

print(f'Get method:\n{w1.get(1)}')

# add

w1.add(m1)
print(f'Adding check:\n{w1}')

# Sorting from larger to smaller, the sorting key is total money(number*amount)

print(f'Sorting:\n{w1.sort()}')

# size

print(f'Size: {w1.size()}\n')

# total balance in tenge

print(f'm1: {m1.to_tenge()}, m2: {m2.to_tenge()}, m3: {m3.to_tenge()}')
print(f'Total balance: {w1.total_balance_in_tenge()}\n')

# __str__

print(f'__str__ checking:\n{w1}')