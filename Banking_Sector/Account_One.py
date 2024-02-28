class InvalidPinException(Exception):
    pass


class InvalidAmountException(Exception):
    pass


class InsufficientFundsException(Exception):
    pass


class Account:
    def __init__(self, accountable, pin):
        self.balance = 0
        self._account_number = accountable
        self.pin = pin
        self._first_name = ""
        self._last_name = ""

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

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    def full_name(self):
        return f"{self._first_name} {self._last_name}"

