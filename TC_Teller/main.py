class user:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return balance


person1 = user("Tommy",999)

print(person1.get_balance())
