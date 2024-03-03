from Exception.insufficient_funds_exception import InsufficientFundsException
from Exception.invalid_amount_exception import InvalidAmountException
from Exception.invalid_pin_exception import InvalidPinException


class Account:
    def __init__(self, account_number, pin, first_name, last_name):
        self.account_number = account_number
        self.pin = pin
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0

    def get_account_number(self):
        return self.account_number

    def first_name(self):
        return self.first_name

    def last_name(self):
        return self.last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def validate_pin(self, entered_pin):
        if self.pin == entered_pin:
            return True
        else:
            raise InvalidPinException("Invalid PIN")

    def get_balance(self, entered_pin):
        if self.validate_pin(entered_pin):
            return self.balance
        else:
            raise InvalidPinException("Invalid PIN")

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountException("Invalid deposit amount")
        self.balance += amount

    def withdraw(self, amount, entered_pin):
        if not self.validate_pin(entered_pin):
            raise InvalidPinException("Invalid PIN")
        if amount <= 0:
            raise InvalidAmountException("Invalid withdrawal amount")
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient funds")
        self.balance -= amount

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def change_pin(self, old_pin, new_pin):
        if not self.validate_pin(old_pin):
            raise InvalidPinException("Invalid PIN")
        else:
            self.pin = new_pin



