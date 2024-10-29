#
# @lc app=leetcode.cn id=36 lang=python3
# @lcpr version=30204
#
# [36] 有效的数独
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                if board[row_idx][col_idx] != "." and not self.check_valid(
                    board, row_idx, col_idx
                ):
                    return False
        return True

    def check_valid(self, board, i, j):
        for row_idx in range(i + 1, len(board)):
            if board[row_idx][j] == board[i][j]:
                return False
        for col_idx in range(j + 1, len(board[0])):
            if board[i][col_idx] == board[i][j]:
                return False
        block_i, block_j = i // 3, j // 3
        for row_idx in range(block_i * 3, block_i * 3 + 3):
            for col_idx in range(block_j * 3, block_j * 3 + 3):
                if (
                    row_idx != i
                    and col_idx != j
                    and board[row_idx][col_idx] == board[i][j]
                ):
                    return False
        return True


# @lc code=end


#
# @lcpr case=start
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

# @lcpr case=start
# [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#
