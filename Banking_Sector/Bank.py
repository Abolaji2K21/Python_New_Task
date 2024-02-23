import random

from Banking_Sector.Account_One import Account


def generate_account_number():
    return random.randint(0, 999999)


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def deposit(self, amount, account_number):
        my_account = self.find_account(account_number)
        if my_account:
            my_account.deposit(amount)
        else:
            return None

    def withdraw(self, amount, account_number, pin):
        my_account = self.find_account(account_number)
        if my_account:
            my_account.withdraw(amount, pin)
        else:
            return None

    def transfer(self, amount, from_account_number, to_account_number, pin):
        source_account = self.find_account(from_account_number)
        destination_account = self.find_account(to_account_number)

        if source_account and destination_account:
            source_account.withdraw(amount, pin)
            destination_account.deposit(amount)

    def check_balance(self, account_number, pin):
        my_account = self.find_account(account_number)

        if my_account:
            if my_account.validate_pin(pin):
                return my_account.get_balance(pin)
            else:
                return None
        else:
            return None

    def register_customer(self, first_name, last_name, pin):
        account_number = generate_account_number()
        my_account = Account(account_number, pin)
        my_account.set_first_name(first_name)
        my_account.set_last_name(last_name)

        self.accounts.append(my_account)
        return my_account

    def remove_account(self, account_number, pin):
        my_account = self.find_account(account_number)
        if my_account and my_account.validate_pin(pin):
            self.accounts.remove(my_account)

    def get_accounts(self):
        return self.accounts
