class BankAccount:
    def __init__(self):
        self._balance = 0.0
        self._transactions = []

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions.append(f"Депозит: +{amount}")
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                self._transactions.append(f"Снятие: -{amount}")
            else:
                print("Недостаточно средств.")
        else:
            print("Сумма должна быть положительной.")

    @property
    def balance(self):
        return self._balance

    def show_transactions(self):
        print("История операций:")
        for t in self._transactions:
            print("-", t)

if __name__ == "__main__":
    acc = BankAccount()
    acc.deposit(1000)
    acc.withdraw(300)
    acc.withdraw(800)
    print(f"Текущий баланс: {acc.balance}")
    acc.show_transactions()

