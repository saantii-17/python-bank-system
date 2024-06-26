# 💸🐍 Banking System in Python

Welcome to the Banking System in Python! This project is an implementation of a basic banking system using Object-Oriented Programming (OOP) in Python. The goal is to provide a platform for learning and practicing OOP, as well as understanding interactions between different entities in a banking environment.
___
## 📑 Features

The system includes the following key features:

- **Clients**: Management of client information and their bank accounts.
- **Bank Accounts**: Creation and management of bank accounts, including deposits, withdrawals, and transfers.
- **Transactions**: Logging and viewing of bank transactions.
- **Ownership Flexibility**: Accounts can exist without an initial owner and can be assigned or transferred between clients.
___
## 🧊 Classes and Methods

### Client

Represents a bank client.

- **Attributes**:
  - `name`: Client's name.
  - `id`: Client's identification.
  - `direction`: Client's address.
  - `contact`: Client's contact information.
  - `accounts`: List of accounts associated with the client.

- **Methods**:
  - `__init__(self, name, id, direction, contact)`: Initializes a new client.
  - `assign_account(self, account)`: Assigns an account to the client.
  - `show_info(self)`: Displays client information.
  - `show_accounts(self)`: Displays client's accounts.

### Account

Represents a bank account.

- **Attributes**:
  - `account_number`: Account number.
  - `type`: Account type (checking, savings).
  - `balance`: Current balance of the account.
  - `transaction_history`: Transaction history of the account.
  - `owner`: Account owner (client).

- **Methods**:
  - `__init__(self, account_number, type, balance=0)`: Initializes a new account.
  - `assign_owner(self, client)`: Assigns an owner to the account.
  - `deposit(self, amount)`: Deposits a specified amount into the account.
  - `withdraw(self, amount)`: Withdraws a specified amount from the account.
  - `show_info(self)`: Displays account information.

### Transaction

Represents a bank transaction.

- **Attributes**:
  - `type`: Transaction type (deposit, withdrawal, transfer).
  - `amount`: Transaction amount.
  - `account`: Account number associated with the transaction.

- **Methods**:
  - `__init__(self, type, amount, account)`: Initializes a new transaction.
  - `show_info(self)`: Displays transaction information.
___
## ⚙ Future improvements

- Graphical interface using `Tkinter`
- Enhanced data management security (hashing)
- Statistics and history
___
## 👨🏼‍🏫 Example Usage

Here's a basic example of how to use the classes defined in this system:

```python
# Create an account
cuenta1 = Cuenta("001", "savings", 1000)

# Create a client
cliente1 = Cliente("John Doe", "98765432", "123 Fake St", "555-4321")

# Assign the account to the client
cliente1.asignar_cuenta(cuenta1)

# Display client and account information
cliente1.mostrar_info()
cuenta1.mostrar_info()
```

___
## ⬇ Installation and Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/your_username/banking-system-python.git
    ```

2. Navigate to the project directory:
    ```bash
    cd banking-system-python
    ```

3. Run the main script:
    ```bash
    python main.py
    ```

___
By [Santi](https://github.com/saantii-17/)
