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
        m, n = len(board), len(board[0])
        for row_idx in range(m):
            if board[row_idx][0] == "O":
                board[row_idx][0] = "T"
                self.dfs(board, row_idx, 0, "O", "T")
            if board[row_idx][n - 1] == "O":
                board[row_idx][n - 1] = "T"
                self.dfs(board, row_idx, n - 1, "O", "T")
        for col_idx in range(n):
            if board[0][col_idx] == "O":
                board[0][col_idx] = "T"
                self.dfs(board, 0, col_idx, "O", "T")
            if board[m - 1][col_idx] == "O":
                board[m - 1][col_idx] = "T"
                self.dfs(board, m - 1, col_idx, "O", "T")

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                    self.dfs(board, i, j, "O", "X")

        for row_idx in range(m):
            if board[row_idx][0] == "T":
                board[row_idx][0] = "O"
                self.dfs(board, row_idx, 0, "T", "O")
            if board[row_idx][n - 1] == "T":
                board[row_idx][n - 1] = "O"
                self.dfs(board, row_idx, n - 1, "T", "O")
        for col_idx in range(n):
            if board[0][col_idx] == "T":
                board[0][col_idx] = "O"
                self.dfs(board, 0, col_idx, "T", "O")
            if board[m - 1][col_idx] == "T":
                board[m - 1][col_idx] = "O"
                self.dfs(board, m - 1, col_idx, "T", "O")

    def dfs(self, board, i, j, source, target):
        directions = {(1, 0), (0, -1), (-1, 0), (0, 1)}
        for direction in directions:
            row, col = i + direction[0], j + direction[1]
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                if board[row][col] == source:
                    board[row][col] = target
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
