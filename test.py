import unittest
from logic import *
from cli import *

class GameTest(unittest.TestCase):

    def test_empty_board_initialization(self):
        board = Board()
        for row in board._rows:
            for cell in row:
                self.assertIsNone(cell)

    def test_two_player_initialization(self):
        game = Game(Human(), Human())
        self.assertIsInstance(game._playerX, Human)
        self.assertIsInstance(game._playerO, Human)

    def test_one_player_initialization(self):
        game = Game(Human(), Bot())
        self.assertIsInstance(game._playerX, Human)
        self.assertIsInstance(game._playerO, Bot)

    def test_player_piece_assignment(self):
        game = Game(Human(), Human())
        self.assertEqual(game._playerX._piece, 'X')
        self.assertEqual(game._playerO._piece, 'O')

    def test_turn_switching(self):
        game = Game(Human(), Human())
        game._current_player = 'O'
        game.make_move(game._playerX)
        self.assertEqual(game._current_player, 'X')

    def test_winning_end_game_detection(self):
        board = Board()
        board.set(0, 0, 'X')
        board.set(1, 1, 'X')
        board.set(2, 2, 'X')
        game = Game(Human(), Bot())
        game._board = board
        winner = game.run()
        self.assertEqual(winner, 'X')

    def test_draw_game_detection(self):
        board = Board()
        board.set(0, 0, 'X')
        board.set(0, 1, 'O')
        board.set(0, 2, 'X')
        board.set(1, 0, 'O')
        board.set(1, 1, 'X')
        board.set(1, 2, 'O')
        board.set(2, 0, 'X')
        board.set(2, 1, 'O')
        board.set(2, 2, 'X')
        game = Game(Human(), Bot())
        game._board = board
        winner = game.run()
        self.assertIsNone(winner)

    def test_viable_spot_restriction(self):
        board = Board()
        board.set(0, 0, 'X')
        game = Game(Human(), Bot())
        game._board = board
        move = game._playerX.get_move(game._board)
        self.assertIsNone(move)

    def test_correct_game_winner_detection(self):
        board = Board()
        board.set(0, 0, 'X')
        board.set(1, 1, 'X')
        board.set(2, 2, 'X')
        game = Game(Human(), Bot())
        game._board = board
        winner = game.run()
        self.assertEqual(winner, 'X')

if __name__ == '__main__':
    unittest.main()