import json


class Money:
    def __init__(self, name: str = 'm1', number: int = 0, currency: str = 'USD', amount: int = 0):
        self.name = name
        self.number = number
        self.currency = currency
        self.amount = amount

    def to_tenge(self):
        total_money = self.amount * self.number
        count = 0
        with open('currency.json') as file:
            currency = json.load(file)
            for i in currency:
                if i['currency'] == self.currency.upper():
                    count += 1
                    return total_money * i['rate']

    def __repr__(self):
        return f'\t{self.name}: (number: {self.number}; currency: {self.currency}; amount: {self.amount});\n'
