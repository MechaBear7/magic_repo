#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30204
#
# [70] 爬楼梯
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 第 i 个台阶可以由第 i-1 和第 i-2 个台阶爬上
        f_2, f_1, f = 0, 0, 1
        for _ in range(n):
            f_2 = f_1
            f_1 = f
            f = f_2 + f_1
        return f


# @lc code=end


#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#
