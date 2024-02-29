# from Bank import Bank
#
#
# class BankApp:
#     def __init__(self):
#         self.bank = Bank("Okay_Bank")
#
#     def display(self):
#         print("""Welcome to Bee_Jays Bank App
#         1. Create Account
#         2. Close Account
#         3. Deposit
#     4. Transfer
#     5. Withdraw
#     6. Check balance
#     7. Exit App""")
#
#     choice = input("Enter your choice: ")
#
#     if choice == '1':
#         create_account()
#     elif choice == '2':
#         close_account()
#     elif choice == '3':
#         deposit()
#     elif choice == '4':
#         transfer()
#     elif choice == '5':
#         withdraw()
#     elif choice == '6':
#         check_balance()
#     elif choice == '7':
#         exit_app()
#     else:
#         print("Invalid choice. Please try again.")
#         display()
#
#
# def exit_app():
#     import sys
#     sys.exit()
#
#
# def close_account():
#     account_number = input("Enter the account number: ")
#     pin = input("Enter your pin: ")
#     try:
#         bank.remove_account(int(account_number), pin)
#         print("Account closed successfully!")
#     except Exception as e:
#         print(str(e))
#     finally:
#         exit_app()
#
#
# def create_account():
#     first_name = input("Enter your first name: ")
#     last_name = input("Enter your last name: ")
#     pin = input("Enter your pin: ")
#     account_number = bank.register_customer(first_name, last_name, pin)
#     print("Account created successfully!")
#     # print(f"Your account number is: {account_number}")
#     display()
#
#
# def deposit():
#     account_number = input("Enter your account number: ")
#     amount = input("Enter an amount: ")
#     try:
#         bank.deposit(int(account_number), int(amount))
#         print("Deposit successful!")
#     except Exception as e:
#         print(str(e))
#     finally:
#         display()
#
#
# def withdraw():
#     account_number = input("Enter your account number: ")
#     amount = input("Enter the amount: ")
#     pin = input("Enter your pin: ")
#     try:
#         bank.withdraw(int(account_number), int(amount), pin)
#         print("Withdrawal successful!")
#     except Exception as e:
#         print(str(e))
#     finally:
#         display()
#
#
# def transfer():
#     amount = input("Enter transfer amount: ")
#     sender_account = input("Enter your account number: ")
#     receiver_account = input("Enter the receiving account number: ")
#     pin = input("Enter your pin: ")
#     try:
#         bank.transfer(int(amount), int(sender_account), int(receiver_account), pin)
#         print("Transfer successful!")
#     except Exception as e:
#         print(str(e))
#     finally:
#         display()
#
#
# def check_balance():
#     account_number = input("Enter your account number: ")
#     pin = input("Enter your pin: ")
#     try:
#         balance = bank.check_balance(int(account_number), pin)
#         print(f"Your balance is: {balance}")
#     except Exception as e:
#         print(str(e))
#     finally:
#         display()
#
#
# def execute():
#     display()
#
#
# if __name__ == "__main__":
#     execute()
