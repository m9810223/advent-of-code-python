def cast_input(inputs):
    bingo, *boards = inputs.split("\n" * 2)

    bingo = [int(x) for x in bingo.split(",")]
    boards = [[[int(x) for x in row.split()] for row in board.split("\n")] for board in boards]
    return bingo, boards


class Board:
    def __init__(self, board):
        self._is_win = False
        self._row_marked = [0] * 5
        self._col_marked = [0] * 5
        self.numbers = {}
        for row in range(5):
            for col in range(5):
                self.numbers[board[row][col]] = (row, col)

    def _mark(self, number):
        row_and_col = self.numbers.pop(number, None)
        if row_and_col:
            row, col = row_and_col
            self._row_marked[row] += 1
            self._col_marked[col] += 1

    def is_win(self, number):
        if self._is_win:
            return False
        self._mark(number)
        self._is_win = 5 in self._row_marked or 5 in self._col_marked
        return self._is_win


def part1(inputs):
    bingo, boards = inputs
    boards = [Board(x) for x in boards]
    for number in bingo:
        for board in boards:
            if board.is_win(number):
                return number * sum(board.numbers)


def part2(inputs):
    bingo, boards = inputs
    boards = [Board(x) for x in boards]
    final_score = None
    for number in bingo:
        for board in boards:
            if board.is_win(number):
                final_score = number * sum(board.numbers)
    return final_score
