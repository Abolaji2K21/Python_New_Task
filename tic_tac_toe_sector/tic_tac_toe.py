from tic_tac_toe_sector.gametype import GameType
from tic_tac_toe_sector.user import User


class TicTacTac:
    def __init__(self, player1, player2):
        self.score_board = [[GameType.EMPTY, GameType.EMPTY, GameType.EMPTY],
                            [GameType.EMPTY, GameType.EMPTY, GameType.EMPTY],
                            [GameType.EMPTY, GameType.EMPTY, GameType.EMPTY]]
        self.players = [player1, player2]
        self.current_player = player1
        self.winner = None
        self.draw = False

    def get_winner(self) -> User:
        return self.winner

    def is_draw(self) -> bool:
        return self.draw

    def get_player(self) -> User:
        return self.players

    def get_score_board(self) -> list:
        return self.score_board

    def get_current_player(self) -> User:
        return self.current_player

    def check_win(self) -> bool:
        for row in range(3):
            if (self.score_board[row][0] == self.current_player.get_type() and
                    self.score_board[row][1] == self.current_player.get_type() and
                    self.score_board[row][2] == self.current_player.get_type()):
                return True

        for column in range(3):
            if (self.score_board[0][column] == self.current_player.get_type() and
                    self.score_board[1][column] == self.current_player.get_type() and
                    self.score_board[2][column] == self.current_player.get_type()):
                return True

        if (self.score_board[0][0] == self.current_player.get_type() and
                self.score_board[1][1] == self.current_player.get_type() and
                self.score_board[2][2] == self.current_player.get_type()):
            return True

        if (self.score_board[0][2] == self.current_player.get_type() and
                self.score_board[1][1] == self.current_player.get_type() and
                self.score_board[2][0] == self.current_player.get_type()):
            return True
        return False

    def check_draw(self) -> bool:
        for row in range(3):
            for cell in row:
                if cell == GameType.EMPTY:
                    return False
        return True




