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
        if not board or not board[0]:
            return

        source, temp, target = "O", "T", "X"

        # Step 1: Mark all 'O's connected to the boundary as 'T'
        for col_idx in range(len(board[0])):
            if board[0][col_idx] == source:
                self.dfs(board, 0, col_idx, source, temp)
            if board[len(board) - 1][col_idx] == source:
                self.dfs(board, len(board) - 1, col_idx, source, temp)
        for row_idx in range(len(board)):
            if board[row_idx][0] == source:
                self.dfs(board, row_idx, 0, source, temp)
            if board[row_idx][len(board[0]) - 1] == source:
                self.dfs(board, row_idx, len(board[0]) - 1, source, temp)

        # Step 2: Change all remaining 'O's to 'X'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == source:
                    board[i][j] = target

        # Step 3: Change all 'T's back to 'O'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == temp:
                    board[i][j] = source

    def dfs(self, board, i, j, source, target):
        board[i][j] = target
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        for direction in directions:
            row, col = i + direction[0], j + direction[1]
            if (
                0 <= row < len(board)
                and 0 <= col < len(board[0])
                and board[row][col] == source
            ):
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
