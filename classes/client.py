'''
TO DO LIST:
    *
'''

class client:
    def __init__(self, name: str, id: int, age: int, email: str):
        self.name = name
        self.id = id
        self.age = age
        self.email = email
        self.accounts = []
    
    def assign_account(self, account):
        self.accounts.append(account)
        print(f'Accounts of this client: {self.accounts}')
    
    def show_info(self):
        print(f'Name: {self.name}')
        print(f'ID: {self.id}')
        print(f'Age: {self.age}')
        print(f'Email: {self.email}')
    
    def show_accounts(self):
        for account in self.accounts:
            print(account)
            print(account.type)
            print(account.balance)
            print('---')