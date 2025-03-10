#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30204
#
# [5] 最长回文子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1
            return s[left + 1: right]

        answer = ""
        for i in range(len(s) - 1):
            for j in (0, 1):
                result = expand(i, i + j)
                if len(result) > len(answer):
                    answer = result
        return answer

# @lc code=end



#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

