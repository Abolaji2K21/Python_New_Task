
from Exception.invalid_pin_exception import InvalidPinException
from User_Diary_Sector.Entry import Entry


class Diary:
    def __init__(self, username: str, password: str):
        if not username:
            raise ValueError("Username cannot be empty.")
        if not password:
            raise ValueError("Password cannot be empty.")
        self.username = username
        self.password = password
        self.entries = []
        self.locked = True

    def get_username(self) -> str:
        return self.username

    def get_password(self) -> str:
        return self.password

    def is_locked(self) -> bool:
        return self.locked

    def get_number_of_entries(self) -> int:
        return len(self.entries)

    def lock_diary(self, password: str) -> None:
        if self.password != password:
            raise ValueError("Incorrect password.")
        self.locked = True

    def unlock_diary(self, password: str) -> None:
        if self.password != password:
            raise InvalidPinException("Incorrect password.")
        self.locked = False

    def create_entry(self, entry_id: int, title: str, body: str) -> None:
        if self.locked:
            raise ValueError("Diary is locked. Cannot add entry.")
        new_entry = Entry(entry_id, title, body)
        self.entries.append(new_entry)

    def find_entry_by_id(self, entry_id: int) -> Entry:
        if self.locked:
            raise ValueError("Diary is locked. Cannot search for entry.")
        for entry in self.entries:
            if entry.get_id() == entry_id:
                return entry
        raise ValueError(f"Entry with id {entry_id} not found.")

    def delete_entry(self, entry_id: int) -> None:
        if self.locked:
            raise ValueError("Diary is locked. Cannot delete entry.")
        for entry_id, entry in enumerate(self.entries):
            if entry.get_id() == entry_id:
                del self.entries[entry_id]
                return
        raise ValueError(f"Entry with id {entry_id} not found.")

    def update_entry(self, entry_id: int, title: str, body: str) -> None:
        if self.locked:
            raise ValueError("Diary is locked. Cannot update entry.")
        entry_to_update = self.find_entry_by_id(entry_id)
        entry_to_update.set_title(title)
        entry_to_update.set_body(body)
