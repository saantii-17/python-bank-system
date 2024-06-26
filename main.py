# Import account class
from account import account

# Print menu options
def menu():
    print('\n')
    print('1. Create account')
    print('2. Delete account')
    print('3. Deposit money')
    print('4. Whithdraw money')
    print('5. Transfer money')
    print('6. Show info')
    print('7. Exit')

# Funcion principal
def main():
    menu()
    option = int(input('Elige una opción: '))
    if option == 1:
        print('Opción 1 seleccionada')
    elif option == 2:
        print('Opción 2 seleccionada')
    elif option == 3:
        print('Opción 3 seleccionada')
    elif option == 4:
        print('Opción 4 seleccionada')
    elif option == 5:
        print('Opción 5 seleccionada')
    elif option == 6:
        print('Opción 6 seleccionada')
    elif option == 7:
        print('Opción 7 seleccionada')
    else:
        exit()

if __name__ == '__main__':
    main()