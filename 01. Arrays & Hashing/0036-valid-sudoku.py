"""
Approach:
1. Use a set to track seen numbers in rows, columns, and 3x3 sub-boxes.
2. Iterate through each cell in the 9x9 board.
3. For each number, check if it violates Sudoku rules by checking if it
    already exists in the corresponding row, column, or 3x3 sub-box.
4. If a violation is found, return False.
5. If no violations are found after checking all cells, return True.

Time Complexity:
O(1) - The size of the board is fixed (9x9), so the time complexity is constant.

Space Complexity:
O(1) - The space required for the set is constant as the board size is fixed.
"""

from typing import List


class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:

        seen = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    if (
                        (i, num) in seen
                        or (num, j) in seen
                        or (i // 3, j // 3, num) in seen
                    ):
                        return False
                    seen.add((i, num))
                    seen.add((num, j))
                    seen.add((i // 3, j // 3, num))

        return True


test = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(test.is_valid_sudoku(board))  # Output: True
