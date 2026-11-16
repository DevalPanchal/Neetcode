'''
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false
'''
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeen = set()
        colSeen = set()
        boxSeen = set()

        for i in range(9):
            for j in range(9):
                digit = board[i][j]

                if digit == ".":
                    continue

                box = (i // 3, j // 3)

                if (i, digit) in rowSeen:
                    return False
                if (j, digit) in colSeen:
                    return False
                if (box, digit) in boxSeen:
                    return False

                rowSeen.add((i, digit))
                colSeen.add((j, digit))
                boxSeen.add((box, digit))

        return True


board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

s = Solution().isValidSudoku(board)
print(s)