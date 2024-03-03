from Banking_Sector.bank import Bank
from Exception.account_not_found_exception import AccountNotFoundException
from Exception.insufficient_funds_exception import InsufficientFundsException
from Exception.invalid_amount_exception import InvalidAmountException
from Exception.invalid_pin_exception import InvalidPinException


class BankApp:
    def __init__(self):
        self.bank = Bank("firstBank")

    def display(self):
        print("")
        print("Bank App")
        print("1.Create customer\n2.Deposit \n3.Transfer \n4.Withdraw\n5.Check balance "
              "\n6.Close Account \n7.Exit App")
        print("---------------------->")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.create_account()
        elif choice == "2":
            self.deposit()
        elif choice == "3":
            self.transfer()
        elif choice == "4":
            self.withdraw()
        elif choice == "5":
            self.check_balance()
        elif choice == "6":
            self.close_account()
        elif choice == "7":
            self.exit()
        else:
            print("Enter valid choice")
            self.display()

    def create_account(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        pin = input("Enter pin: ")
        account = self.bank.register_customer(first_name, last_name, pin)
        print("Customer registered successfully!")
        print("Account Number: ", account.get_account_number())

        self.display()

    def deposit(self):
        account_number = input("Enter your account number: ")
        amount = float(input("Enter an amount to deposit: "))
        try:
            self.bank.deposit(account_number, amount)
        except AccountNotFoundException as e:
            print(e)
        finally:
            self.display()

    def transfer(self):
        sender_account = input("Enter your account number: ")
        receiver_account = input("Enter the receiver account number: ")
        amount = float(input("Enter transfer amount: "))
        pin = input("Enter your pin: ")
        try:
            self.bank.transfer(amount, sender_account, receiver_account, pin)
            print("Amount transferred successfully!")
        except (InsufficientFundsException, AccountNotFoundException, InvalidPinException) as e:
            print(e)
        finally:
            self.display()

    def withdraw(self):
        account_number = input("Enter your account number: ")
        amount = float(input("Enter the amount to withdraw: "))
        pin = input("Enter your pin: ")
        try:
            self.bank.withdraw(account_number, amount, pin)
            print("Amount withdrawn successfully!")
        except (InvalidAmountException, InvalidPinException, InsufficientFundsException, AccountNotFoundException) as e:
            print(e)
        finally:
            self.display()

    def check_balance(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        try:
            balance = self.bank.check_balance(account_number, pin)
            print("Your balance is:", balance)
        except (InvalidPinException, AccountNotFoundException) as e:
            print(e)
        finally:
            self.display()

    def close_account(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your pin: ")
        try:
            self.bank.remove_account(account_number, pin)
            print("Account closed successfully!")
        except (InvalidPinException, AccountNotFoundException) as e:
            print(e)
        finally:
            self.display()

    @staticmethod
    def exit():
        print("Exit")


def main():
    bank_app = BankApp()
    bank_app.display()


if __name__ == "__main__":
    main()
