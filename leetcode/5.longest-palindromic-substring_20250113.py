"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-13 10:59:34
LastEditors: Helei.Yang
LastEditTime: 2025-01-13 11:06:10
FilePath: /magic_repo/leetcode/5.longest-palindromic-substring_20250113.py
Description: 
"""

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
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        ans = ""
        for i in range(len(s)):
            for j in (0, 1):
                result = expand_from_center(i, i+j)
                ans = result if len(result) > len(ans) else ans
        return ans
# @lc code=end



#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

