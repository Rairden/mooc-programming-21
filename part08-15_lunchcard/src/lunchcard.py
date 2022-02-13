class LunchCard:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def eat_lunch(self):
        if self.balance >= 2.6:
            self.balance -= 2.6

    def eat_special(self):
        if self.balance >= 4.6:
            self.balance -= 4.6

    def deposit_money(self, deposit):
        if deposit < 0:
            raise ValueError("deposit needs to be positive")
        self.balance += deposit


petersCard = LunchCard(20)
gracesCard = LunchCard(30)
petersCard.eat_special()
gracesCard.eat_lunch()
print(f"Peter: {petersCard}")
print(f"Grace: {gracesCard}")

petersCard.deposit_money(20)
gracesCard.eat_special()
print(f"Peter: {petersCard}")
print(f"Grace: {gracesCard}")

petersCard.eat_lunch()
petersCard.eat_lunch()
gracesCard.deposit_money(50)
print(f"Peter: {petersCard}")
print(f"Grace: {gracesCard}")
