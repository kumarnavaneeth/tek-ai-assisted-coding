class BankAccount:
    def __init__(self,intial_balance=0,notification_system=None):
        if intial_balance <0:
            raise ValueError("Initial balance cannot be negative")
        self.balance=intial_balance
        self.notification_system=notification_system

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        if self.notification_system:
            self.notification_system.notify(amount, self.balance)

    def get_balance(self):
        return self.balance