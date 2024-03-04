import unittest

from tic_tac_toe_sector.gametype import GameType
from tic_tac_toe_sector.user import User
from tic_tac_toe_sector.tic_tac_toe import TicTacTac


class MyTestCase(unittest.TestCase):

    def test_that_creation_of_tic_tac_toe_game_with_2_player_is_valid(self):
        player1 = User(1, 1)
        player2 = User(2, 2)

        my_game = TicTacTac(player1, player2)
        self.assertListEqual([player1, player2], my_game.get_players())

    def test_to_ensure_that_the_game_has_a_score_board_that_is_initialized_correctly_with_an_empty(self):
        player1 = User(1, 1)
        player2 = User(2, 2)

        my_game = TicTacTac(player1, player2)
        self.assertListEqual([[GameType.EMPTY, GameType.EMPTY, GameType.EMPTY],
                              [GameType.EMPTY, GameType.EMPTY, GameType.EMPTY],
                              [GameType.EMPTY, GameType.EMPTY, GameType.EMPTY]], my_game.get_score_board())


