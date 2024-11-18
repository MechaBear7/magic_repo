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
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1
            return s[left + 1 : right]

        max_ans = ""
        for i in range(len(s)):
            for j in (0, 1):
                ans = expand_around_center(s, i, i + j)
                max_ans = max_ans if len(max_ans) > len(ans) else ans

        return max_ans


# @lc code=end


#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#
