'''
TO DO LIST:
    *Improve transaction_history show_info()
'''

class account:
    def __init__(self, account_number: int, type: str, balance=0):
        self.account_number = account_number
        self.type = type
        self.balance = balance
        self.transaction_history = []
    
    def assign_owner(self, client):
        self.owner = client
        print(f'{self.owner} has been established as the owner of this account')
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Your actual account balance is {self.balance}€') 

    def whithdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print('Money has been withdraw succesfuly')
            print(f'Your actual balance is {self.balance}€')
        else:
            print('You do not have enough money')
    
    def show_info(self):
        print(f'Account_number: {self.account_number}')
        print(f'Type of account: {self.type}')
        print(f'Balance: {self.balance}€')
        print(f'Transaction history: {self.transaction_history}')
        print(f'Owner: {self.owner}')