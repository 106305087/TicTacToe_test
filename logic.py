class Board:
    def __init__(self):
        self._rows = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def __str__(self):
        s = '-------\n'
        for row in self._rows:
            for cell in row:
                s += '|' + (cell if cell is not None else ' ')
            s += '|\n-------\n'
        return s

    def get(self, x, y):
        return self._rows[y][x]

    def set(self, x, y, value):
        if 0 <= x < 3 and 0 <= y < 3:
            self._rows[y][x] = value

    def get_winner(self):
        # Check rows, columns, and diagonals
        lines = self._rows + [list(col) for col in zip(*self._rows)] + \
                [[self._rows[i][i] for i in range(3)], [self._rows[i][2-i] for i in range(3)]]

        for line in lines:
            if line.count(line[0]) == 3 and line[0] is not None:
                return line[0]
        return None
