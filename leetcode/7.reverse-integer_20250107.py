"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-07 14:38:34
LastEditors: Helei.Yang
LastEditTime: 2025-01-07 14:41:20
FilePath: /codes/magic_repo/leetcode/7.reverse-integer_20250107.py
Description: 
"""

#
# @lc app=leetcode.cn id=7 lang=python3
# @lcpr version=30204
#
# [7] 整数反转
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -(1 << 31), (1 << 31) - 1
        negative = x < 0
        x = abs(x)
        new_num = 0
        while x > 0:
            new_num = new_num * 10 + x % 10
            x = x // 10
        if negative:
            new_num = - new_num
        if new_num < INT_MIN or new_num > INT_MAX:
            return 0
        return new_num
        

# @lc code=end



#
# @lcpr case=start
# 123\n
# @lcpr case=end

# @lcpr case=start
# -123\n
# @lcpr case=end

# @lcpr case=start
# 120\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

#

