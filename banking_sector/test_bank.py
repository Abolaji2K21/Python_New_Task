import unittest
from banking_sector.bank import Bank
from Exception.account_not_found_exception import AccountNotFoundException
from Exception.invalid_pin_exception import InvalidPinException


class TestBank(unittest.TestCase):

    def test_registration_of_more_than_two_customers(self):
        bank = Bank("Bee_jayBank")
        my_account = bank.register_customer("Am", "Tired", "1234")
        my_account1 = bank.register_customer("Am", "Frustrated", "4321")
        my_account2 = bank.register_customer("Am", "Angry", "2356")

        self.assertEqual(3, len(bank.get_accounts()))

    def test_register_customer(self):
        bank = Bank("Bee_jayBank")
        my_account = bank.register_customer("Am", "Tired", "1234")
        self.assertEqual("Am Tired", my_account.full_name())  # Corrected method call

    def test_that_after_registration_you_can_delete_an_account(self):
        bank = Bank("Bee_jayBank")
        my_account = bank.register_customer("Am", "Tired", "1234")
        my_account1 = bank.register_customer("Am", "Frustrated", "4321")
        my_account2 = bank.register_customer("Am", "Angry", "2356")

        bank.remove_account(my_account1.get_account_number(), "4321")

        self.assertEqual(2, len(bank.get_accounts()))

    def test_that_after_registration_you_can_delete_an_account_twice(self):
        bank = Bank("Bee_jayBank")
        my_account = bank.register_customer("Am", "Tired", "1234")
        my_account1 = bank.register_customer("Am", "Frustrated", "4321")
        my_account2 = bank.register_customer("Am", "Angry", "2356")

        bank.remove_account(my_account1.get_account_number(), "4321")
        bank.remove_account(my_account.get_account_number(), "1234")  # Corrected method and attribute access

        self.assertEqual(1, len(bank.get_accounts()))

    def test_that_after_registration_you_can_not_delete_an_account_after_a_wrong_pin(self):
        bank = Bank("Bee_jayBank")
        my_account = bank.register_customer("Am", "Tired", "1234")

        bank.remove_account(my_account.get_account_number(), "1345")  # Corrected method and attribute access
        self.assertEqual(1, len(bank.get_accounts()))

    def test_that_you_can_deposit(self):
        bank = Bank("Bee_jayBank")
        my_account = bank.register_customer("Am", "Tired", "1234")
        account_number = my_account.get_account_number()  # Corrected method access

        bank.deposit(account_number, 1000)
        self.assertEqual(1000, my_account.get_balance("1234"))

    def test_that_you_can_deposit_twice(self):
        bank = Bank("Bee_jayBank")
        my_account = bank.register_customer("Am", "Tired", "1234")
        account_number = my_account.get_account_number()  # Corrected method access

        bank.deposit(account_number, 1000)
        bank.deposit(account_number, 1000)
        self.assertEqual(2000, my_account.get_balance("1234"))

    def test_deposit_raises_account_not_found_exception(self):
        bank = Bank("Bee_jayBank")
        with self.assertRaises(AccountNotFoundException):
            bank.deposit(123, 1000)
