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
        for row in range(1, m):
            dp[row][0] = 1 if dp[row - 1][0] == 1 and obstacleGrid[row][0] == 0 else 0
        for col in range(1, n):
            dp[0][col] = 1 if dp[0][col - 1] == 1 and obstacleGrid[0][col] == 0 else 0
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
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

