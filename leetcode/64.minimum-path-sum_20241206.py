#
# @lc app=leetcode.cn id=64 lang=python3
# @lcpr version=30204
#
# [64] 最小路径和
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for row in range(1, m):
            dp[row][0] = dp[row - 1][0] + grid[row][0]
        for col in range(1, n):
            dp[0][col] = dp[0][col - 1] + grid[0][col]
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])
        return dp[-1][-1]


# @lc code=end


#
# @lcpr case=start
# [[1,3,1],[1,5,1],[4,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#
