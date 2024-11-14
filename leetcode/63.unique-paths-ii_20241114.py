#
# @lc app=leetcode.cn id=63 lang=python3
# @lcpr version=30204
#
# [63] 不同路径 II
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] != 1 else 0
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] != 1 else 0

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] if obstacleGrid[i][j] != 1 else 0

        return dp[-1][-1]


# @lc code=end


#
# @lcpr case=start
# [[0,0,0],[0,1,0],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,0]]\n
# @lcpr case=end

#
