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
                left -= 1
                right += 1
            return left + 1, right  # Adjusted to return the exact palindrome bounds

        max_len = 0
        max_ans = ""

        for i in range(len(s)):
            # Expand around center for both even and odd length palindromes
            for j in (0, 1):  # j=0 -> odd length, j=1 -> even length
                left, right = expand_around_center(s, i, i + j)
                current_len = right - left
                if current_len > max_len:
                    max_len = current_len
                    max_ans = s[left:right]

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
