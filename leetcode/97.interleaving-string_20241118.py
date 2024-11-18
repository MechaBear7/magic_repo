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
        if len(s3) != len(s1) + len(s2):
            return False
        # dp[i][j] 表示 s3 的前 i+j 个字符是否可以由 s1 的前 i 个字符和 s2 的前 j 个字符组成
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
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
