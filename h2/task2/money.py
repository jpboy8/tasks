import json


class Money:
    def __init__(self, name: str = 'm1', number: int = 0, currency: str = 'USD', amount: int = 0):
        self.name = name
        self.number = number
        self.currency = currency
        self.amount = amount

    def to_tenge(self):
        total_money = self.amount * self.number

        with open('currency.json') as file:
            currency = json.load(file)
            for key, value in currency.items():
                if key == self.currency.upper():
                    return total_money * value

    def __repr__(self):
        return f'\t{self.name}: (number: {self.number}; currency: {self.currency}; amount: {self.amount});\n'
