class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        # input: 9*9 2D array
        # conditions: each row has 1-9 NO DUPLICATES
                    # each column has 1-9 NO DUPLICATES
                    # Each of the 9 values in sub-boxes must have 1-9 NO DUPLICATES
        # output: boolean if valid or no

        # Hash Set, dict

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True