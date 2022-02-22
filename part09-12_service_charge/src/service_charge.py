class BankAccount:
    def __init__(self, owner, accountID, balance):
        self.__owner = owner
        self.__accountID = accountID
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def withdraw(self, amt):
        self.__balance -= amt
        self.__service_charge()

    def deposit(self, amt):
        self.__balance += amt
        self.__service_charge()

    def __service_charge(self):
        percentChange = self.__balance * 0.01
        self.__balance -= percentChange


if __name__ == '__main__':
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)
