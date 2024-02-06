class PhoneBook:
    userChoice = 0
    contacts = {}

    def __init__(self):
        self.input = input

    def main(self):
        while True:
            self.userChoice = self.welcome()
            if self.userChoice == 1:
                if self.displayContacts():
                    print("Loading >>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print("Displayed successfully.")
                else:
                    print("Loading >>> >>>  >>>>  >>>>>>>>>> >>>>>>>")
                    print("Failed to load contacts.")
                    print("No contacts available.")
            elif self.userChoice == 2:
                name = input("Enter name: ")
                num = int(input("Enter Phone Number: "))
                if self.create_contact(name, num):
                    print("Creating Contact.")
                    print("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print("Contact Created Successfully")
                    print()
                else:
                    print("Loading >>> >>>  >>>>  >>>>>>>>>> >>>>>>>")
                    print("Failed to create contact.")
            elif self.userChoice == 3:
                name = input("Enter name: ")
                if self.checkEntry(name):
                    print("Searching  >>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print("Wawu!!! Contact found.")
                else:
                    print("Searching  >>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print("Whoops!!! Contact not found.")
            elif self.userChoice == 4:
                name = input("Enter contact name to delete: ")
                if self.deleteEntry(name):
                    print("Loading >>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print("Contact deleted successfully.")
                else:
                    print("Loading >>> >>>  >>>>  >>>>>>>>>> >>>>>>>")
                    print("Failed to delete contact.")
            elif self.userChoice == 5:
                print("Exiting >>> >>>  >>>>  >>>>>>>>>> >>>>>>>")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def setUserChoice(self, choice):
        self.userChoice = choice

    def getUserChoice(self):
        return self.userChoice

    def welcome(self):
        print("Welcome To Phone_Book :")
        print(">>> Bjay Contact Book Command are : 1,2,3,4 or 5 <<<")
        print(">>> What Would You Like To Do? <<<")
        print("[1]. Display Your Existing Contacts")
        print("[2]. Create a New Contact")
        print("[3]. Check An Entry ")
        print("[4]. Delete An Entry")
        print("[5]. Exit")
        print()
        return int(input("Enter Your Entry here (1, 2, 3, 4 or 5): "))

    def deleteEntry(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False

    def checkEntry(self, name):
        return name in self.contacts

    def displayContacts(self):
        print("Existing Contacts:")
        if self.contacts:
            for name, number in self.contacts.items():
                print("Name: ", name)
                print("Number: ", number)
            return True
        return False

    def create_contact(self, name, num):
        if name not in self.contacts:
            self.contacts[name] = num
            return True
        return False

# phone_book = PhoneBook()
# phone_book.main()
