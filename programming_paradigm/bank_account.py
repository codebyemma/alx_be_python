class BankAccount:
    def __init__(self, amount=0):
        self.account_balance = amount
    def deposit(self, amount):
        total = self.account_balance + amount
        self.account_balance = total
        return amount
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return amount
        else:
            return False
    def display_balance(self):
        return self.account_balance