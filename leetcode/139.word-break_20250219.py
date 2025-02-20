#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30204
#
# [139] 单词拆分
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True  # dp[i] 代表 s[:i] 能否由 wordDict 组成
        for i in range(1, len(s) + 1):
            if not dp[i-1]:
                continue
            for word in wordDict:
                if s[i-1:i-1+len(word)] == word:
                    dp[i-1+len(word)] = True
        return dp[-1]

# @lc code=end



#
# @lcpr case=start
# "leetcode"\n["leet", "code"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple", "pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats", "dog", "sand", "and", "cat"]\n
# @lcpr case=end

#

