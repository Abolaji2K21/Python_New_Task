from Exception.invalid_user_ID_exception import InvalidUserIDException
from Exception.null_game_type_exception import NullGameTypeException
from tic_tac_toe_sector.gametype import GameType


class User:
    def __init__(self, entry_id, game_type):
        if entry_id <= 0:
            raise InvalidUserIDException("ID must be a positive integer")
        if game_type is None:
            raise NullGameTypeException("GameType must be specified")
        self.entry_id = entry_id
        self.game_type = game_type

    def get_id(self):
        return self.entry_id

    def get_game_type(self):
        return self.game_type

    def play_game(self, row: str, column: str):
        pass
