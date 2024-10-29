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
        # 临时标记 "T"，代表格子被访问
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    check = self.check_surrounded(board, i, j)
                    if check:
                        self.write(board, i, j, "X")
                    else:
                        self.write(board, i, j, "O")

    def write(self, board, i, j, data):
        board[i][j] = data
        directions = {(1, 0), (0, -1), (-1, 0), (0, 1)}
        for direction in directions:
            row = i + direction[0]
            col = j + direction[1]
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                if board[row][col] == "T":
                    self.write(board, row, col, data)

    def check_surrounded(self, board, i, j):
        directions = {(1, 0), (0, -1), (-1, 0), (0, 1)}
        if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
            return False
        elif board[i][j] != "O":
            return True
        else:
            board[i][j] = "T"
            check = True
            for direction in directions:
                row, col = direction[0] + i, direction[1] + j
                if 0 <= row < len(board) and 0 <= col < len(board[0]):
                    if board[row][col] == "O":
                        check = check and self.check_surrounded(board, row, col)
            return check


# @lc code=end


#
# @lcpr case=start
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]\n
# @lcpr case=end

# @lcpr case=start
# [["X"]]\n
# @lcpr case=end

#
