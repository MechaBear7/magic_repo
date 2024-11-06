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
                if board[i][j] != "." and not self.check_valid(board, i, j):
                    return False

        return True

    def check_valid(self, board, i, j):
        cur_num = board[i][j]
        m, n = len(board), len(board[0])
        # 同一行
        for col in range(j + 1, n):
            if board[i][col] == cur_num:
                return False
        # 同一列
        for row in range(i + 1, m):
            if board[row][j] == cur_num:
                return False
        # 九宫格
        b_i, b_j = i // 3, j // 3
        for row in range(b_i * 3, b_i * 3 + 3):
            for col in range(b_j * 3, b_j * 3 + 3):
                if row == i and col == j:
                    continue
                if board[row][col] == cur_num:
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
