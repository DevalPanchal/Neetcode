'''
You are given an m x n 2-D integer array matrix and an 
integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer 
of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?
'''
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            print(f"({row}, {col}) {target} {matrix[row][col]}")
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1

        return False

matrix = [
    [1,2,4,8],
    [10,11,12,13],
    [14,20,30,40]
]

target = 10
res = Solution().searchMatrix(matrix, target)
print(res)

