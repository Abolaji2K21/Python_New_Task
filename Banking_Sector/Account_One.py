class InvalidPinException(Exception):
    pass


class InvalidAmountException(Exception):
    pass


class InsufficientFundsException(Exception):
    pass


class Account:
    def __init__(self, accountable, pin):
        self.balance = 0
        self.accountnumber = accountable
        self.pin = pin
        self.firstName = ""
        self.lastName = ""

    def validate_pin(self, key):
        return self.pin == key

    def get_balance(self, pin):
        if not self.validate_pin(pin):
            raise InvalidPinException("Invalid PIN")
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount, pin):
        if not self.validate_pin(pin):
            raise InvalidPinException("Invalid PIN")
        if amount < 0:
            raise InvalidAmountException("Invalid withdrawal amount")
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient funds")
        self.balance -= amount

    def get_account_number(self):
        return self.accountnumber

    def set_first_name(self, first_name):
        self.firstName = first_name

    def set_last_name(self, last_name):
        self.lastName = last_name

    def get_first_name(self):
        return self.firstName

    def get_last_name(self):
        return self.lastName

    def get_full_name(self):
        return f"{self.firstName} {self.lastName}"
