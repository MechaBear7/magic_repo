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
        directions = {(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)}
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 检查当前点周围一共有几个活细胞
                count = 0
                for direction in directions:
                    row, col = i + direction[0], j + direction[1]
                    if 0 <= row < len(board) and 0 <= col < len(board[0]):
                        if abs(board[row][col]) == 1:
                            count += 1
                if board[i][j] == 1:
                    if count > 3 or count < 2:
                        board[i][j] = -1  # 活细胞死亡
                else:
                    if count == 3:
                        board[i][j] = 2  # 死细胞复活

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


# @lc code=end


#
# @lcpr case=start
# [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,0]]\n
# @lcpr case=end

#
