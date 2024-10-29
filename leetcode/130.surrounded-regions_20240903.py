#
# @lc app=leetcode.cn id=130 lang=python3
# @lcpr version=30204
#
# [130] 被围绕的区域
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_row = len(board)
        num_col = len(board[0])

        for row_idx in range(len(board)):
            if board[row_idx][0] == "O":
                self.dfs(board, row_idx, 0, "O", "T")
            if board[row_idx][num_col - 1] == "O":
                self.dfs(board, row_idx, num_col - 1, "O", "T")
        for col_idx in range(len(board[0])):
            if board[0][col_idx] == "O":
                self.dfs(board, 0, col_idx, "O", "T")
            if board[num_row - 1][col_idx] == "O":
                self.dfs(board, num_row - 1, col_idx, "O", "T")

        for i in range(num_row):
            for j in range(num_col):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for row_idx in range(len(board)):
            if board[row_idx][0] == "T":
                self.dfs(board, row_idx, 0, "T", "O")
            if board[row_idx][num_col - 1] == "T":
                self.dfs(board, row_idx, num_col - 1, "T", "O")
        for col_idx in range(len(board[0])):
            if board[0][col_idx] == "T":
                self.dfs(board, 0, col_idx, "T", "O")
            if board[num_row - 1][col_idx] == "T":
                self.dfs(board, num_row - 1, col_idx, "T", "O")

    def dfs(self, board, i, j, source, target):
        board[i][j] = target
        directions = {(1, 0), (0, -1), (-1, 0), (0, 1)}
        for direction in directions:
            row = i + direction[0]
            col = j + direction[1]
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                if board[row][col] == source:
                    self.dfs(board, row, col, source, target)


# @lc code=end


#
# @lcpr case=start
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]\n
# @lcpr case=end

# @lcpr case=start
# [["X"]]\n
# @lcpr case=end

#
