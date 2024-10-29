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
                if board[i][j] != ".":
                    if not self.checkValid(board, i, j):
                        return False
        return True

    def checkValid(self, board, i, j):
        target = board[i][j]

        # 检查横向是否有重复
        for col_idx in range(len(board[0])):
            if col_idx != j and board[i][col_idx] == target:
                return False

        # 检查纵向是否有重复
        for row_idx in range(len(board)):
            if row_idx != i and board[row_idx][j] == target:
                return False

        # 检查九宫格是否有重复
        bi, bj = i // 3 * 3, j // 3 * 3
        for row_idx in range(bi, bi + 3):
            for col_idx in range(bj, bj + 3):
                if (row_idx != i or col_idx != j) and board[row_idx][col_idx] == target:
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
