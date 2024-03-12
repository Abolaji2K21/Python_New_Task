from User_Diary_Sector.diaries import Diaries
from User_Diary_Sector.diary import Diary


class DiaryApp:
    def __init__(self):
        self.my_diary = Diary('username', 'password')
        self.my_diaries = Diaries()

    def main_menu(self) -> None:
        self.welcome()
        print("""
            1 --> Create Diary
            2 --> Lock Diary
            3 --> Unlock Diary
            4 --> Create Entry
            5 --> Find Entry By Id
            6 --> Update Entry
            7 --> Delete Entry
            8 --> Exit App
        """)
        print("Kindly enter any choice from the above:")
        choice = input("still waiting :")
        if choice:
            self.handle_choice(choice)

    def handle_choice(self, choice):
        choice = choice.strip()[0]
        if choice == '1':
            self.create_diary()
        elif choice == '2':
            self.lock_diary()
        elif choice == '3':
            self.unlock_diary()
        elif choice == '4':
            self.create_entry()
        elif choice == '5':
            self.find_entry_by_id()
        elif choice == '6':
            self.update_entry()
        elif choice == '7':
            self.delete_entry()
        elif choice == '8':
            self.exit_app()
        else:
            self.main_menu()

    def delete_entry(self):
        entry_id = input("Kindly Enter The Unique Id Of The Entry: ")
        try:
            self.my_diary.delete_entry(int(entry_id))
            print("Entry deleted successfully.")
        except Exception as e:
            print(e)
        finally:
            self.main_menu()

    def lock_diary(self):
        password = input("Enter password To Lock Diary: ")
        try:
            self.my_diary.lock_diary(password)
            print("Diary locked successfully.")
        except Exception as e:
            print(e)
        finally:
            self.main_menu()

    def unlock_diary(self):
        password = input("Enter password To Unlock Diary: ")
        try:
            self.my_diary.unlock_diary(password)
            print("Diary unlocked successfully.")
        except Exception as e:
            print(e)
        finally:
            self.main_menu()

    def create_diary(self):
        username = input("Kindly Enter A username Of Your Choice: ")
        password = input("Kindly Enter A passkey Of Your Choice: ")
        try:
            self.my_diaries.add_diary(username, password)
            print("Diary Created successfully.")
        except Exception as e:
            print(e)
        finally:
            self.main_menu()

    def find_entry_by_id(self):
        entry_id = input("Kindly Enter The Unique Id Of The Entry: ")
        try:
            entry = self.my_diary.find_entry_by_id(int(entry_id))
            print("Entry found successfully:", entry)
        except Exception as e:
            print(e)
        finally:
            self.main_menu()

    def create_entry(self):
        entry_id = input("Kindly Enter The Unique Id Of The Entry: ")
        title = input("Kindly Enter The Title Of The Entry: ")
        body = input("Kindly Enter The Body Of The Entry: ")
        try:
            self.my_diary.create_entry(int(entry_id), title, body)
            print("Entry created successfully.")
        except Exception as e:
            print(e)
        finally:
            self.main_menu()

    def update_entry(self):
        entry_id = input("Kindly Enter The Unique Id Of The Entry To Update: ")
        new_title = input("Kindly Enter The New Title Of The Entry: ")
        new_body = input("Kindly Enter The New Body Of The Entry: ")
        try:
            self.my_diary.update_entry(int(entry_id), new_title, new_body)
            print("Entry updated successfully.")
        except Exception as e:
            print(e)
        finally:
            self.main_menu()

    @staticmethod
    def exit_app():
        print("Exiting App.")
        print(">>>>>>>>>>>>>>>>>>>>.")
        import sys
        sys.exit(0)

    @staticmethod
    def welcome() -> None:
        print("Welcome To AppByMeDiary\n")
        print("The next page Displays And Help You With Your Choice ?\n")


if __name__ == "__main__":
    app = DiaryApp()
    app.main_menu()
