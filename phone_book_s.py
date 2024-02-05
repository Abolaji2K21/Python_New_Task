class PhoneBook_s:
    userChoice = 0
    name = ""
    #input = None
    contactName = []
    contactNumber = []

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
                if self.deleteEntry():
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
        #name = input("Enter contact name to delete: ")
        index = self.contactName.index(name) if name in self.contactName else -1
        if index != -1:
            del self.contactName[index]
            del self.contactNumber[index]

    def checkEntry(self, name):
       # name = input("Enter contact name to check: ")
        return name in self.contactName


    def displayContacts(self):
        print("Existing Contacts:")
        if self.contactName:
            for index in range(len(self.contactName)):
                print("Name: ", self.contactName[index])
                print()
                print("Number: ", self.contactNumber[index])


    def create_contact(self, name, num):
        self.contactName.append(name)
        self.contactNumber.append(num)

#phone_book = PhoneBook_s()
#phone_book.main()

