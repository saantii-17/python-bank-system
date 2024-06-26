import random

class account:
    def __init__(self, name):
        self.id = random.randint(0, 999)
        self.balance = 0
        self.name = name
    def 