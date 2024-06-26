""" # Import account class
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
    main() """

class Cliente:
    def __init__(self, nombre, identificacion, direccion, contacto):
        self.nombre = nombre
        self.identificacion = identificacion
        self.direccion = direccion
        self.contacto = contacto
        self.cuentas = []

    def crear_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, ID: {self.identificacion}, Dirección: {self.direccion}, Contacto: {self.contacto}")
        for cuenta in self.cuentas:
            cuenta.mostrar_info()

class Cuenta:
    def __init__(self, numero_cuenta, tipo, balance=0):
        self.numero_cuenta = numero_cuenta
        self.tipo = tipo
        self.balance = balance
        self.historial_transacciones = []

    def depositar(self, monto):
        self.balance += monto
        transaccion = Transaccion('depósito', monto, self.numero_cuenta)
        self.historial_transacciones.append(transaccion)

    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
            transaccion = Transaccion('retiro', monto, self.numero_cuenta)
            self.historial_transacciones.append(transaccion)
        else:
            print("Fondos insuficientes")

    def mostrar_info(self):
        print(f"Cuenta {self.numero_cuenta} ({self.tipo}), Balance: {self.balance}")

class Transaccion:
    def __init__(self, tipo, monto, cuenta):
        self.tipo = tipo
        self.monto = monto
        self.cuenta = cuenta

    def mostrar_info(self):
        print(f"Transacción: {self.tipo}, Monto: {self.monto}, Cuenta: {self.cuenta}")

# Ejemplo de uso
cliente1 = Cliente("Juan Perez", "12345678", "Calle Falsa 123", "555-1234")
cuenta1 = Cuenta("001", "ahorro", 1000)
cliente1.crear_cuenta(cuenta1)
cliente1.mostrar_info()
