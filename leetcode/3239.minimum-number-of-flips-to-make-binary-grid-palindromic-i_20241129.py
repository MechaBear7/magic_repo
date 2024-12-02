#
# @lc app=leetcode.cn id=3239 lang=python3
# @lcpr version=30204
#
# [3239] 最少翻转次数使二进制矩阵回文 I
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_ans = 0
        for row in range(m):
            left, right = 0, n - 1
            while left < right:
                if grid[row][left] != grid[row][right]:
                    row_ans += 1
                left, right = left + 1, right - 1
        col_ans = 0
        for col in range(n):
            top, bottom = 0, m - 1
            while top < bottom:
                if grid[top][col] != grid[bottom][col]:
                    col_ans += 1
                top, bottom = top + 1, bottom - 1

        return min(row_ans, col_ans)


# @lc code=end


#
# @lcpr case=start
# [[1,0,0],[0,0,0],[0,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,1],[0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1],[0]]\n
# @lcpr case=end

#
