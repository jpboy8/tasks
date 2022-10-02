from money import Money


class Wallet(Money):
    def __init__(self, money: list([])):
        for i in money:
            name = i.name
            number = i.number
            currency = i.currency
            amount = i.amount
        Money.__init__(self, name, number, currency, amount)
        self.__moneys = money

    @property
    def moneys(self):
        return self.__moneys

    @moneys.setter
    def moneys(self, value):
        if isinstance(value, list):
            self.__moneys = value
        else:
            raise ValueError("value must be a list!")

    def get(self, index: int = 0):
        return self.moneys[index]

    def add(self, money):
        self.moneys.append(money)

    def size(self):
        return len(self.moneys)

    def sort(self):
        chars = '[],'
        rez = ''.join(i for i in str(sorted(self.moneys, key=lambda x: -x.number * x.amount)) if i not in chars)
        return rez

    def total_balance_in_tenge(self):
        total = 0

        for i in self.moneys:
            total += i.to_tenge()

        return total

    def __repr__(self):
        rez = ''

        for money in self.moneys:
            rez += money.__repr__()

        return rez
