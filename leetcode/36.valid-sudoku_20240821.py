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
        for i in range(9):
            for j in range(9):
                if not board[i][j].isalnum():
                    continue
                if not self.pass_check(board, i, j):
                    return False
        return True

    def pass_check(self, board, row_idx, col_idx):
        # 检查纵向是否有重复
        for i in range(row_idx + 1, 9):
            if board[i][col_idx] == board[row_idx][col_idx]:
                return False
        # 检查横向是否有重复
        for j in range(col_idx + 1, 9):
            if board[row_idx][j] == board[row_idx][col_idx]:
                return False
        # 检查九宫格内是否有重复
        block_i = row_idx // 3
        block_j = col_idx // 3
        count = 0
        for i in range(3):
            for j in range(3):
                if board[block_i * 3 + i][block_j * 3 + j] == board[row_idx][col_idx]:
                    count += 1
        return count == 1


# @lc code=end


#
# @lcpr case=start
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

# @lcpr case=start
# [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#
