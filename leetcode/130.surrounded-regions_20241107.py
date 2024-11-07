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
        src, tar = "O", "T"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i != 0 and i != len(board) - 1 and j != 0 and j != len(board[0]) - 1:
                    continue
                if board[i][j] == src:
                    board[i][j] = tar
                    self.dfs(board, i, j, src, tar)

        src, tar = "O", "X"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == src:
                    board[i][j] = tar
                    self.dfs(board, i, j, src, tar)

        src, tar = "T", "O"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i != 0 and i != len(board) - 1 and j != 0 and j != len(board[0]) - 1:
                    continue
                if board[i][j] == src:
                    board[i][j] = tar
                    self.dfs(board, i, j, src, tar)

    def dfs(self, board, i, j, src, tar):
        directions = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        for direction in directions:
            row, col = i + direction[0], j + direction[1]
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                if board[row][col] == src:
                    board[row][col] = tar
                    self.dfs(board, row, col, src, tar)


# @lc code=end


#
# @lcpr case=start
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]\n
# @lcpr case=end

# @lcpr case=start
# [["X"]]\n
# @lcpr case=end

#
