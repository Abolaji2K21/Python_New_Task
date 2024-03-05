from datetime import datetime


class Entry:
    def __init__(self, entry_id, title, body):
        self.entry_id = entry_id
        self.title = title
        self.body = body
        self.date_created = datetime.now()

    def get_id(self):
        return self.entry_id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def set_title(self, title):
        self.title = title

    def set_body(self, body):
        self.body = body

