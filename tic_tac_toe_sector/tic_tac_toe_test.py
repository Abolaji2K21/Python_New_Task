import unittest

from Exception.cell_occupied_exception import CellOccupiedException
from Exception.invalid_user_ID_exception import InvalidUserIDException
from Exception.null_game_type_exception import NullGameTypeException
from tic_tac_toe_sector.gametype import GameType
from tic_tac_toe_sector.user import User
from tic_tac_toe_sector.tic_tac_toe import TicTacTac


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.player1 = User(1, 1)
        self.player2 = User(2, 2)
        self.my_game = TicTacTac(self.player1, self.player2)

    def test_that_creation_of_tic_tac_toe_game_with_2_player_is_valid(self):
        # player1 = User(1, 1)
        # player2 = User(2, 2)
        #
        # my_game = TicTacTac(player1, player2)
        self.assertListEqual([self.player1, self.player2], self.my_game.get_players())

    def test_to_ensure_that_the_game_has_a_score_board_that_is_initialized_correctly_with_an_empty(self):
        player1 = User(1, 1)
        player2 = User(2, 2)

        my_game = TicTacTac(player1, player2)
        self.assertListEqual([[GameType.EMPTY, GameType.EMPTY, GameType.EMPTY],
                              [GameType.EMPTY, GameType.EMPTY, GameType.EMPTY],
                              [GameType.EMPTY, GameType.EMPTY, GameType.EMPTY]], my_game.get_score_board())

    def test_that_i_can_get_current_player(self):
        # player1 = User(1, 1)
        # player2 = User(2, 2)
        #
        # my_game = TicTacTac(player1, player2)
        self.assertListEqual([self.player1, self.player2], self.my_game.get_players())
        self.assertListEqual([[GameType.EMPTY, GameType.EMPTY, GameType.EMPTY],
                              [GameType.EMPTY, GameType.EMPTY, GameType.EMPTY],
                              [GameType.EMPTY, GameType.EMPTY, GameType.EMPTY]], self.my_game.get_score_board())

        self.my_game.make_move(1, 0)
        self.assertEqual(self.player2, self.my_game.get_current_player())

    def test_that_a_player_can_not_play_in_a_cell_that_is_already_occupied(self):
        player1 = User(1, 1)
        player2 = User(2, 2)

        my_game = TicTacTac(player1, player2)
        self.assertListEqual([player1, player2], my_game.get_players())
        self.assertListEqual([[GameType.EMPTY, GameType.EMPTY, GameType.EMPTY],
                              [GameType.EMPTY, GameType.EMPTY, GameType.EMPTY],
                              [GameType.EMPTY, GameType.EMPTY, GameType.EMPTY]], my_game.get_score_board())

        my_game.make_move(1, 0)
        self.assertEqual(player2, my_game.get_current_player())
        my_game.make_move(2, 1)
        self.assertEqual(player1, my_game.get_current_player())
        with self.assertRaises(CellOccupiedException):
            my_game.make_move(2, 1)

    def test_constructor_with_null_game_type(self):
        with self.assertRaises(NullGameTypeException):
            self.player1 = User(1, None)

    def test_constructor_with_invalid_user_id_exception(self):
        with self.assertRaises(InvalidUserIDException):
            self.player2 = User(-1, 2)

    def test_negative_row_value_exception(self):
        with self.assertRaises(IndexError):
            self.my_game.make_move(-1, 0)

    def test_negative_column_value_exception(self):
        with self.assertRaises(IndexError):
            self.my_game.make_move(1, -3)

    def test_negative_diagonal_value_exception(self):
        with self.assertRaises(IndexError):
            self.my_game.make_move(1, -1)

    def test_positive_row_value_exception_can_not_be_greater_than_three(self):
        with self.assertRaises(IndexError):
            self.my_game.make_move(4, 2)

    def test_positive_column_value_exception_can_not_be_greater_than_three(self):
        with self.assertRaises(IndexError):
            self.my_game.make_move(2, 3)
