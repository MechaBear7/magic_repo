"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-13 11:28:08
LastEditors: Helei.Yang
LastEditTime: 2025-01-13 11:40:23
FilePath: /magic_repo/leetcode/43.multiply-strings_20250113.py
Description: 

"""

#
# @lc app=leetcode.cn id=43 lang=python3
# @lcpr version=30204
#
# [43] 字符串相乘
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        flg1 = 1
        for i in reversed(range(len(num1))):
            flg2 = 1
            for j in reversed(range(len(num2))):
                result += flg1 * int(num1[i]) * flg2 * int(num2[j])
                flg2 *= 10
            flg1 *= 10
        return str(result)

# @lc code=end



#
# @lcpr case=start
# "2"\n"3"\n
# @lcpr case=end

# @lcpr case=start
# "123"\n"456"\n
# @lcpr case=end

#

