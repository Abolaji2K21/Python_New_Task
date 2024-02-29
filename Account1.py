from decimal import Decimal

class Account1:
    def __init__(self, name , balance: Decimal):
        self.name = name
        self.set_balance(balance)


    @oriorty
    def balance(self):
        return  self.balance

    @balance.setter
    def set_balance(self, balance: Decimal):
        if balance < Decimal(0.00):

            raise ValueError("Invalid amount for balance")
        self.balance = balance




