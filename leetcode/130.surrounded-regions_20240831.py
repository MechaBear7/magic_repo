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
        self.write_edge(board, "O", "M")
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                    self.dfs(board, i, j, "O", "X")
        self.write_edge(board, "M", "O")

    def write_edge(self, board, s1, s2):
        left, right, top, bottom = 0, len(board[0]) - 1, 0, len(board) - 1
        for col in range(left, right + 1):
            if board[top][col] == s1:
                board[top][col] = s2
                self.dfs(board, top, col, s1, s2)
        for row in range(top + 1, bottom + 1):
            if board[row][right] == s1:
                board[row][right] = s2
                self.dfs(board, row, right, s1, s2)
        for col in range(right - 1, left - 1, -1):
            if board[bottom][col] == s1:
                board[bottom][col] = s2
                self.dfs(board, bottom, col, s1, s2)
        for row in range(bottom - 1, top, -1):
            if board[row][left] == s1:
                board[row][left] = s2
                self.dfs(board, row, left, s1, s2)

    def dfs(self, board, i, j, s1, s2):
        directions = {(1, 0), (0, -1), (-1, 0), (0, 1)}
        for direction in directions:
            row, col = i + direction[0], j + direction[1]
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                if board[row][col] == s1:
                    board[row][col] = s2
                    self.dfs(board, row, col, s1, s2)


# @lc code=end


#
# @lcpr case=start
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]\n
# @lcpr case=end

# @lcpr case=start
# [["X"]]\n
# @lcpr case=end

#
