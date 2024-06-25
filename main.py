from account import account
from client import client

# Print menu options
def menu():
    print('1. Create account')
    print('2. Delete account')
    print('3. Deposit money')
    print('4. Whithdraw money')
    print('5. Transfer money')
    print('6. Show info')

# Funcion principal
def main():
    menu()

if __name__ == '__main__':
    main()