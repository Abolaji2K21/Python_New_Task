from User_Diary_Sector.diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def get_number_of_diaries(self):
        diaries_count = len(self.diaries)
        return diaries_count

    def add_diary(self, username: str, password: str):
        my_diary = Diary(username, password)
        self.diaries.append(my_diary)

    def delete_diary(self, username: str, password: str):
        self.diaries = [my_diary for my_diary in self.diaries
                        if my_diary.get_username() != username or my_diary.get_password() != password]

    def find_by_username(self, username: str):
        for my_diary in self.diaries:
            if my_diary.get_username() == username:
                return my_diary
        raise ValueError(f"Username {username} not found.")
