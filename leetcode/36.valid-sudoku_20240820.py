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
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j].isalnum() and not self.check(board, i, j):
                    # print(i, j)
                    return False
        return True

    def check(self, board, row_idx, col_idx):
        num_row = len(board)
        num_col = len(board[0])
        for i in range(row_idx + 1, num_row):
            if board[i][col_idx] == board[row_idx][col_idx]:
                return False
        for j in range(col_idx + 1, num_col):
            if board[row_idx][j] == board[row_idx][col_idx]:
                return False
        block_i = row_idx // 3
        bolck_j = col_idx // 3
        count = 0
        for i in range(3):
            for j in range(3):
                if board[block_i * 3 + i][bolck_j * 3 + j] == board[row_idx][col_idx]:
                    count += 1
        if count > 1:
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
