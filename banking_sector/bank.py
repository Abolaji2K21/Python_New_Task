from banking_sector.account_One import Account
from Exception.account_not_found_exception import AccountNotFoundException
from Exception.insufficient_funds_exception import InsufficientFundsException
from Exception.invalid_amount_exception import InvalidAmountException
from Exception.invalid_pin_exception import InvalidPinException


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def find_account(self, account_number):
        for my_account in self.accounts:
            if my_account.account_number() == account_number:
                return my_account
        raise AccountNotFoundException("Account not found")

    def deposit(self, account_number, amount):
        try:
            my_account = self.find_account(account_number)
            my_account.deposit(amount)
        except AccountNotFoundException as e:
            raise e

    def withdraw(self, account_number, amount, pin):
        try:
            my_account = self.find_account(account_number)
            my_account.withdraw(amount, pin)
        except AccountNotFoundException as e:
            raise e
        except (InvalidAmountException, InvalidPinException, InsufficientFundsException) as e:
            raise e

    def transfer(self, amount, from_account_number, to_account_number, pin):
        try:
            source_account = self.find_account(from_account_number)
            destination_account = self.find_account(to_account_number)
            source_account.withdraw(amount, pin)
            destination_account.deposit(amount)
        except AccountNotFoundException as e:
            raise e
        except (InvalidAmountException, InvalidPinException, InsufficientFundsException) as e:
            raise e

    def check_balance(self, account_number, pin):
        try:
            my_account = self.find_account(account_number)
            if my_account.validate_pin(pin):
                return my_account.get_balance()
        except AccountNotFoundException as e:
            raise e
        except InvalidPinException as e:
            raise e

    def register_customer(self, first_name, last_name, pin):
        account_number = self.generate_account_number()
        my_account = Account(first_name + " " + last_name, pin, account_number)
        self.accounts.append(my_account)
        return my_account

    def remove_account(self, account_number, pin):
        try:
            my_account = self.find_account(account_number)
            if my_account.validate_pin(pin):
                self.accounts.remove(my_account)
        except AccountNotFoundException as e:
            raise e
        except InvalidPinException as e:
            raise e

    def generate_account_number(self):
        self.counter += 1
        return self.counter

    def number_of_customers(self):
        return len(self.accounts)
