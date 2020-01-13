from copy import deepcopy


class NQueens:
    def __init__(self, N):
        self.N = N
        self.K = 1
        self.Outputs = {}

    def print_sol(self, board):
        print(f'On {self.K}th Solution')
        self.Outputs[self.K] = []
        self.Outputs[self.K] += deepcopy(board)
        self.K += 1

    def is_safe(self, board, row, col):
        for i in range(col):
            if board[row][i]:  # Checking if that particular cell already has a queen.
                return False

        i = row
        j = col
        # checking if there is a queen on upper diagonal on left side
        while i >= 0 and j >= 0:
            if board[i][j]:  # Again checking  if there's a queen
                return False
            j -= 1
            i -= 1

        i = row
        j = col
        while j >= 0 and i < self.N:
            if board[i][j]:
                return False
            i += 1
            j -= 1

            # Finally, that place is safe to place our beautiful queen!
        return True

    def solve_util(self, board, col):
        """
        First, it checks if all the queens are placed, and then returns true...
        """
        try:
            if col == self.N:
                self.print_sol(board)
                return True

                # Trying to place this queen in all rows one by one
            res = False
            for i in range(self.N):
                if self.is_safe(board, i, col):
                    board[i][col] = 1
                    res = self.solve_util(board, col + 1) or res
                    if type(res) == dict:
                        return res
                    board[i][col] = 0  # Backtracking...

            # if queen cannot be placed in any row in this col, then alas
            # we return false..
            return res
        except KeyboardInterrupt:
            print('Keyboard Interrupted!')
            return self.Outputs

    def solve(self):
        board = [[0 for j in range(self.N)] for i in range(self.N)]
        outputs = self.solve_util(board, 0)
        if not outputs:
            print('No solution exists.')
            return False
        return outputs


def main():
    NQueens(20).solve()


if __name__ == "__main__":
    main()
