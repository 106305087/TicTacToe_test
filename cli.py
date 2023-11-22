from logic import Board
import random

class Game:
    def __init__(self, playerX, playerO):
        self._board = Board()
        self._playerX = playerX
        self._playerO = playerO
        self._current_player = 'X'  # Start with player X

    def make_move(self, player):
        valid_move = False
        while not valid_move:
            move = player.get_move(self._board)
            if move is None:
                continue
            x, y = move
            if self._board.get(x, y) is None:
                self._board.set(x, y, self._current_player)
                valid_move = True
            else:
                print('Spot taken. Try again.')

        self._current_player = 'O' if self._current_player == 'X' else 'X'

    def run(self):
        while self._board.get_winner() is None and not self.is_board_full():
            print(self._board)
            current_player = self._playerX if self._current_player == 'X' else self._playerO
            self.make_move(current_player)

        print(self._board)
        winner = self._board.get_winner()
        if winner:
            print(f'{winner} won!')
        else:
            print("It's a draw")

    def is_board_full(self):
        return all(cell is not None for row in self._board._rows for cell in row)

class Human:
    def get_move(self, board):
        while True:
            try:
                row, col = map(int, input('Enter row and column (1-3): ').split())
                if 1 <= row <= 3 and 1 <= col <= 3:
                    return row - 1, col - 1
                else:
                    print('Row and column numbers must be between 1 and 3. Please try again.')
            except ValueError:
                print('Invalid input. Please enter two numbers separated by space.')

class Bot:
    def get_move(self, board):
        available = [(x, y) for x in range(3) for y in range(3) if board.get(x, y) is None]
        return random.choice(available) if available else None

if __name__ == '__main__':
    game = Game(Human(), Bot())
    game.run()
