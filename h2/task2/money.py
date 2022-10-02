import json


class Money:
    def __init__(self, name: str = 'm1', number: int = 0, currency: str = 'USD', amount: int = 0):
        self.__name = name
        self.__number = number
        self.__currency = currency
        self.__amount = amount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Name must be a string!")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if type(value) not in (int, float) or value < 0:
            raise ValueError("Number must be integer or float and positive!")
        self.__number = value

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        if isinstance(value, str):
            self.__currency = value
        else:
            raise ValueError("Currency must be string")

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if type(value) not in (int, float) or value < 0:
            raise ValueError("Number must be integer or float and positive!")
        self.__amount = value

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
