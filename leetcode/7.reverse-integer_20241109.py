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

        is_negative = True if x < 0 else False
        x = abs(x)

        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        
        result = -result if is_negative else result
        if result < INT_MIN or result > INT_MAX:
            return 0
        else:
            return result

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

