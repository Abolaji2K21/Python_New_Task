import unittest
from decimal import Decimal

from Scripts.Account import Account


class MyTestCase(unittest.TestCase):

    def test_newAccountBalanceIsZero(self):
        my_account: Account = Account("Bee jay", Decimal(0))
        expected = 0
        self.assertEqual(expected, my_account.getbalance())

    def test_deposit10k_balance10k(self):
        my_account: Account = Account("Bee jay", Decimal(0))
        my_account.deposit(10_000)
        expected = 10_000
        self.assertEqual(expected, my_account.getbalance())

    def test_deposit10Ktwice_balance20k(self):
        my_account: Account = Account("Bee jay", Decimal(0))
        my_account.deposit(10_000)
        my_account.deposit(10_000)

        expected = 20_000
        self.assertEqual(expected, my_account.getbalance())

    def test_deposit_negative10K_balance0k(self):
        my_account: Account = Account("Bee jay", Decimal(0))
        my_account.deposit(-10_000)
        expected = 0
        self.assertEqual(expected, my_account.getbalance())

