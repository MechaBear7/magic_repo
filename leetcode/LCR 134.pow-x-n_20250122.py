"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-22 16:42:56
LastEditors: Helei.Yang
LastEditTime: 2025-01-22 16:47:31
FilePath: /magic_repo/leetcode/LCR 134.pow-x-n_20250122.py
Description: 
"""

#
# @lc app=leetcode.cn id=LCR 134 lang=python3
# @lcpr version=30204
#
# [LCR 134] Pow(x, n)
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        negative = n < 0
        n = abs(n)
        odd = n % 2 == 1
        half_res = self.myPow(x, n // 2)
        result = half_res * half_res if not odd else half_res * half_res * x
        if negative:
            result = 1 / result
        return result

# @lc code=end



#
# @lcpr case=start
# 2.00000\n10\n
# @lcpr case=end

# @lcpr case=start
# 2.10000\n3\n
# @lcpr case=end

# @lcpr case=start
# 2.00000\n-2\n
# @lcpr case=end

#

