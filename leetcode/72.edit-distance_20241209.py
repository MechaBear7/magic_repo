#
# @lc app=leetcode.cn id=72 lang=python3
# @lcpr version=30204
#
# [72] 编辑距离
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for row in range(1, m + 1):
            dp[row][0] = row
        for col in range(1, n + 1):
            dp[0][col] = col
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                right_op = dp[row - 1][col - 1] if word1[row - 1] == word2[col - 1] else dp[row - 1][col - 1] + 1
                dp[row][col] = min(dp[row - 1][col] + 1, dp[row][col - 1] + 1, right_op)
        return dp[-1][-1]


# @lc code=end


#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#
