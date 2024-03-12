import unittest

from Exception.invalid_pin_exception import InvalidPinException
from banking_sector.account_One import Account
from Exception.insufficient_funds_exception import InsufficientFundsException
from Exception.invalid_amount_exception import InvalidAmountException


class TestAccount(unittest.TestCase):

    def test_newly_created_account_has_zero_balance(self):
        account = Account("Bee_Jay", "1234", 0)
        self.assertEqual(0, account.check_balance("1234"))

    def testAccountPinThrowsException_whenInvalidPinIsInputWhenCreatingAccount(self):
        account = Account("Bee_Jay", "1234", 0)
        with self.assertRaises(InvalidPinException):
            account.check_balance("12ergshr")

    def testDepositNegativeAmount_ThrowsException(self):
        account = Account("Bee_Jay", "1234", 0)
        with self.assertRaises(InvalidAmountException):
            account.deposit(-5000)
            account.check_balance("1234")

    def testDepositAmount_BalanceIncreases(self):
        account = Account("Bee_Jay", "1234", 0)
        account.deposit(10_000)
        self.assertEqual(10_000, account.check_balance("1234"))

    def test_withdrawNegativeAmount_ThrowsExceptionTest(self):
        account = Account("Bee_Jay", "1234", 0)
        account.deposit(10_000)
        with self.assertRaises(InsufficientFundsException):
            account.withdraw(-5000, "1234")

    def test_withdrawMoreThanAccountBalance_ThrowsException(self):
        account = Account("Bee_Jay", "1234", 0)
        account.deposit(10_000)
        with self.assertRaises(InsufficientFundsException):
            account.withdraw(15000, "1234")

    def test_enterIncorrectPinUponWithdrawal_ThrowException(self):
        account = Account("Bee_Jay", "1234", 0)
        account.deposit(10_000)
        with self.assertRaises(InvalidPinException):
            account.withdraw(5000, "1i34")

