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
        def expand_center(s, i, j):
            left, right = i, j
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1
            return s[left + 1 : right]

        result = ""
        for i in range(len(s)):
            for j in (0, 1):
                res = expand_center(s, i, i + j)
                if len(res) > len(result):
                    result = res
        return result


# @lc code=end


#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#
