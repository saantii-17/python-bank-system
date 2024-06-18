import random

'''
CALSES PRINCIPALES
* Cliente
* Cuenta
OPERACIONES BASICAS
* Depositar
* Retirar
* Transferencia
SEGURIDAD
*Contraseña
GESTION DE CUENTAS Y CLIENTES
* Crear cuentas
* Eliminar cuentas
* Actualizar información cliente
REPORTES Y ESTADÍSTICAS
* Estado de cuentas
* Gráficos y estadisticas
* Historial (ultima trasnsaccion, ingresos...etc)
'''

class client:
    def __init__(self, name):
        self.name = name
        self.id = random.randint(0, 9999)
        self.accounts = []

    def show_info(self):
        print(f'Name: {self.name}')
        print(f'ID: {self.id}')
        print(f'Accoutns: {self.accounts}')
    
    def add_account(self, cuenta):
        if isinstance(cuenta, account):
            self.accounts.append(cuenta)

#====================================================================    

class account:
    def __init__(self, owner):
        if not isinstance(owner, client):
            raise TypeError('The owner must be an existant client')
        self.owner = owner
        self.id = random.randint(000, 9999)
        self.balance = 0
        owner.add_account(self)

    def show_info(self):
        print(f'Owner: {self.owner}')
        print(f'ID: {self.id}')
        print(f'Balance: {self.balance}€')

    def change_owner(self, new_owner: str):
        self.owner = new_owner
        print(f'The owner has been changed to {self.owner}')

    def change_balance(self, deposit: int):
        self.balance = self.balance + deposit
        print(f'Balance: {self.balance}€')

#====================================================================
cliente1 = client('Santi')
my_account = account(cliente1)
for i in cliente1.accounts:
    print(f'{i.balance}, {i.id}')