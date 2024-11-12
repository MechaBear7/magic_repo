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
        def expand_around_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1
            return s[left + 1 : right]

        max_len, max_res = 0, ""
        for i in range(len(s)):
            for j in (0, 1):
                result = expand_around_center(s, i, i + j)
                if len(result) > max_len:
                    max_res = result
                    max_len = len(result)

        return max_res


# @lc code=end


#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#
