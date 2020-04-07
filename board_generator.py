import random


class board_generator:
    def __init__(self,m=3):
        self.m = m
        self.n = m**2
        """Return a random filled m**2 x m**2 Sudoku board."""
        self.board = [[None for _ in range(self.n)] for _ in range(self.n)]

    def search(self,c=0):
        "Recursively search for a solution starting at position c."
        i, j = divmod(c, self.n)
        i0, j0 = i - i % self.m, j - j % self.m  # Origin of mxm block
        numbers = list(range(1, self.n + 1))
        random.shuffle(numbers)
        for x in numbers:
            if (x not in self.board[i]  # row
                    and all(row[j] != x for row in self.board)  # column
                    and all(x not in row[j0:j0 + self.m]  # block
                            for row in self.board[i0:i])):
                self.board[i][j] = x
                if c + 1 >= self.n ** 2 or self.search(c + 1):
                    return self.board
        else:
            # No number is valid in this cell: backtrack and try again.
            self.board[i][j] = None
            return None


    def make_board(self):
        self.search()
        #print(self.board)

    def remove(self):
        for k in range(0, 70):
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            self.board[i][j] = 0

    def get_board(self):
        self.make_board()
        self.remove()
        return self.board
    #print(remove(make_board()))

