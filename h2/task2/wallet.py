class Wallet():
    def __init__(self, money: list([])):
        self.moneys = money

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
        chars = '[],'
        filtered_list = ''.join(i for i in str(self.moneys) if i not in chars)

        return filtered_list