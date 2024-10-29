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
        # 检查横向是否满足
        for col_index in range(j + 1, len(board[0])):
            if board[i][col_index] == board[i][j]:
                return False
        # 检查纵向是否满足
        for row_index in range(i + 1, len(board)):
            if board[row_index][j] == board[i][j]:
                return False
        # 检查九宫格是否满足
        count = 0
        I, J = i // 3, j // 3
        for i_ in range(3):
            for j_ in range(3):
                if board[I * 3 + i_][J * 3 + j_] == board[i][j]:
                    count += 1
        if count == 0:
            raise ValueError
        elif count > 1:
            return False
        else:
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
