class BankAccount:
    
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.interest_rate = 0.01
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def set_interest_rate(self, rate):
        self.interest_rate = rate
        
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        
    def get_balance(self):
        return self.balance