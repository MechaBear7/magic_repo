#
# @lc app=leetcode.cn id=289 lang=python3
# @lcpr version=30204
#
# [289] 生命游戏
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = {(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)}
        m = len(board)
        n = len(board[0])

        for row_idx in range(m):
            for col_idx in range(n):
                lives_count = 0
                for direction in directions:
                    new_row_idx = row_idx + direction[0]
                    new_col_idx = col_idx + direction[1]
                    if 0 <= new_row_idx < m and 0 <= new_col_idx < n:
                        if abs(board[new_row_idx][new_col_idx]) == 1:
                            lives_count += 1
                if board[row_idx][col_idx] == 1:  # 当前是活细胞
                    if lives_count < 2 or lives_count > 3:
                        board[row_idx][col_idx] = -1  # 活细胞死亡
                elif lives_count == 3:
                        board[row_idx][col_idx] = 2  # 死细胞复活
        print(board)
        for row_idx in range(m):
            for col_idx in range(n):
                if board[row_idx][col_idx] == -1:
                    board[row_idx][col_idx] = 0
                if board[row_idx][col_idx] == 2:
                    board[row_idx][col_idx] = 1
# @lc code=end



#
# @lcpr case=start
# [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,0]]\n
# @lcpr case=end

#

