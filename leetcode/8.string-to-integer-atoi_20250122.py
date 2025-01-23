"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-22 16:37:11
LastEditors: Helei.Yang
LastEditTime: 2025-01-22 16:41:57
FilePath: /magic_repo/leetcode/8.string-to-integer-atoi_20250122.py
Description: 
"""

#
# @lc app=leetcode.cn id=8 lang=python3
# @lcpr version=30204
#
# [8] 字符串转换整数 (atoi)
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        while idx < len(s) and s[idx] == " ":
            idx += 1
        if idx == len(s):
            return 0
        negative = s[idx] == "-"
        if s[idx] in ("+", "-"):
            idx += 1
        result = 0
        while idx < len(s) and ord("0") <= ord(s[idx]) <= ord("9"):
            result = 10 * result + int(s[idx])
            idx += 1
        INT_MIN, INT_MAX = -(1 << 31), (1 << 31) - 1
        
        result = -result if negative else result
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result
# @lc code=end



#
# @lcpr case=start
# "42"\n
# @lcpr case=end

# @lcpr case=start
# " -042"\n
# @lcpr case=end

# @lcpr case=start
# "1337c0d3"\n
# @lcpr case=end

# @lcpr case=start
# "0-1"\n
# @lcpr case=end

# @lcpr case=start
# "words and 987"\n
# @lcpr case=end

#

