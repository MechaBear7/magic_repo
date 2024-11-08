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
        INT_MIN = -(1 << 31)
        INT_MAX = (1 << 31) - 1

        is_negative = x < 0
        if is_negative:
            x = -x

        reversed_x = 0
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x = x // 10

        reversed_x = -reversed_x if is_negative else reversed_x

        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        else:
            return reversed_x


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
