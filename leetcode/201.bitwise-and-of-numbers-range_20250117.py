"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-17 12:51:56
LastEditors: Helei.Yang
LastEditTime: 2025-01-17 13:21:55
FilePath: /magic_repo/leetcode/201.bitwise-and-of-numbers-range_20250117.py
Description: 
"""

#
# @lc app=leetcode.cn id=201 lang=python3
# @lcpr version=30204
#
# [201] 数字范围按位与
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            cnt += 1
        return left << cnt

# @lc code=end



#
# @lcpr case=start
# 5\n7\n
# @lcpr case=end

# @lcpr case=start
# 0\n0\n
# @lcpr case=end

# @lcpr case=start
# 1\n2147483647\n
# @lcpr case=end

#

