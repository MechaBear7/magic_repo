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
        for row_idx in range(len(board)):
            if board[row_idx][0] == src:
                board[row_idx][0] = tar
                self.dfs(board, row_idx, 0, src, tar)
            if board[row_idx][len(board[0]) - 1] == src:
                board[row_idx][len(board[0]) - 1] = tar
                self.dfs(board, row_idx, len(board[0]) - 1, src, tar)
        for col_idx in range(len(board[0])):
            if board[0][col_idx] == src:
                board[0][col_idx] = tar
                self.dfs(board, 0, col_idx, src, tar)
            if board[len(board) - 1][col_idx] == src:
                board[len(board) - 1][col_idx] = tar
                self.dfs(board, len(board) - 1, col_idx, src, tar)

        src, tar = "O", "X"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == src:
                    board[i][j] = tar
                    self.dfs(board, i, j, src, tar)

        src, tar = "T", "O"
        for row_idx in range(len(board)):
            if board[row_idx][0] == src:
                board[row_idx][0] = tar
                self.dfs(board, row_idx, 0, src, tar)
            if board[row_idx][len(board[0]) - 1] == src:
                board[row_idx][len(board[0]) - 1] = tar
                self.dfs(board, row_idx, len(board[0]) - 1, src, tar)
        for col_idx in range(len(board[0])):
            if board[0][col_idx] == src:
                board[0][col_idx] = tar
                self.dfs(board, 0, col_idx, src, tar)
            if board[len(board) - 1][col_idx] == src:
                board[len(board) - 1][col_idx] = tar
                self.dfs(board, len(board) - 1, col_idx, src, tar)

    def dfs(self, board, i, j, src, tar):
        directions = {(-1, 0), (0, 1), (1, 0), (0, -1)}
        for direction in directions:
            row_idx = i + direction[0]
            col_idx = j + direction[1]
            if (row_idx < 0 or row_idx >= len(board)) or (
                col_idx < 0 or col_idx >= len(board[0])
            ):
                continue
            if board[row_idx][col_idx] == src:
                board[row_idx][col_idx] = tar
                self.dfs(board, row_idx, col_idx, src, tar)


# @lc code=end


#
# @lcpr case=start
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]\n
# @lcpr case=end

# @lcpr case=start
# [["X"]]\n
# @lcpr case=end

#
