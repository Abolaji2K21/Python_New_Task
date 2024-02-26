from User_Diary_Sector.Entry import Entry


class InvalidPinException(Exception):
    pass


class Diary:
    def __init__(self, username, password):
        if not username:
            raise ValueError("You need a username to create a diary")
        if not password:
            raise ValueError("You need a password to create a diary")

        self.username = username
        self.password = password
        self.is_locked = True
        self.entries = []

    def get_number_of_entries(self):
        return len(self.entries)

    def unlock_diary(self, password):
        if self.password == password:
            self.is_locked = False
        else:
            raise InvalidPinException("Wrong Password kindly enter a new one")

    def lock_diary(self):
        self.password = None
        self.is_locked = True

    def is_locked(self):
        return self.is_locked

    def create_entry(self, entry_id, title, body):
        new_entry = Entry(entry_id, title, body)
        self.entries.append(new_entry)

    def delete_entry(self, entry_id):
        self.entries = [entry for entry in self.entries if entry.id != entry_id]

    def find_entry_by_id(self, entry_id):
        for entry in self.entries:
            if entry.id == entry_id:
                return entry
        return None

    def update_entry(self, entry_id, title, body):
        for entry in self.entries:
            if entry.id == entry_id:
                entry.title = title
                entry.body = body
                return
        raise ValueError("Entry ID Not Found")

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password
