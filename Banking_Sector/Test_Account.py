from unittest import TestCase

import unittest
from Banking_Sector.Account_One import Account, InsufficientFundsException, InvalidAmountException, InvalidPinException


class TestAccount(unittest.TestCase):

    def test_default_state_of_my_account(self):
        my_account = Account(123456768, "2458")
        self.assertEqual(0, my_account.get_balance("2458"))

    def test_deposit_negative_balance_balance_remain_unchanged(self):
        my_account = Account(123456768, "2458")
        self.assertEqual(0, my_account.get_balance("2458"))
        my_account.deposit(-50_000)
        self.assertEqual(0, my_account.get_balance("2458"))

    def test_deposit_positive_amount_balance_increase(self):
        my_account = Account(123456768, "2458")
        self.assertEqual(0, my_account.get_balance("2458"))
        my_account.deposit(2_000)
        self.assertEqual(2_000, my_account.get_balance("2458"))

    def test_deposit_positive_amount_twice_balance_increases(self):
        my_account = Account(123456768, "2458")
        self.assertEqual(0, my_account.get_balance("2458"))
        my_account.deposit(2_000)
        my_account.deposit(4_000)
        self.assertEqual(6_000, my_account.get_balance("2458"))

    def test_withdraw_negative_amount_balance_remain_unchanged(self):
        my_account = Account(123456768, "2458")
        self.assertEqual(0, my_account.get_balance("2458"))
        with self.assertRaises(InvalidAmountException):
            my_account.withdraw(-20_000, "2458")
        self.assertRaises(InvalidAmountException, my_account.withdraw, -20_000, "2458")

    def test_withdraw_positive_amount_balance_changes(self):
        my_account = Account(123456768, "2458")
        self.assertEqual(0, my_account.get_balance("2458"))
        my_account.deposit(1_200)
        my_account.withdraw(1000, "2458")
        self.assertEqual(200, my_account.get_balance("2458"))

    def test_withdraw_positive_amount_twice_balance_changes(self):
        my_account = Account(123456768, "2458")
        my_account.deposit(1_200)
        my_account.withdraw(1_000, "2458")
        my_account.withdraw(200, "2458")
        self.assertEqual(0, my_account.get_balance("2458"))

    def test_withdraw_positive_amount_is_greater_than_balance_balance_remains_unchanged(self):
        my_account = Account(123456768, "2458")
        my_account.deposit(200)
        with self.assertRaises(InsufficientFundsException):
            my_account.withdraw(1_200, "2458")
