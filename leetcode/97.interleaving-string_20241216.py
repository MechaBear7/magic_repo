#
# @lc app=leetcode.cn id=97 lang=python3
# @lcpr version=30204
#
# [97] 交错字符串
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        dp[0][0] = True
        for row in range(1, n1 + 1):
            dp[row][0] = dp[row - 1][0] if s3[row - 1] == s1[row - 1] else False
        for col in range(1, n2 + 1):
            dp[0][col] = dp[0][col - 1] if s3[col - 1] == s2[col - 1] else False
        for row in range(1, n1 + 1):
            for col in range(1, n2 + 1):
                dp[row][col] = (dp[row - 1][col] and s1[row - 1] == s3[row + col - 1]) or (dp[row][col - 1] and s2[col - 1] == s3[row + col - 1])
        return dp[-1][-1]


# @lc code=end


#
# @lcpr case=start
# "aabcc"\n"dbbca"\n"aadbbcbcac"\n
# @lcpr case=end

# @lcpr case=start
# "aabcc"\n"dbbca"\n"aadbbbaccc"\n
# @lcpr case=end

# @lcpr case=start
# ""\n""\n""\n
# @lcpr case=end

#
