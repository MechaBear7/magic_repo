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
        current_step = 1  # 当前台阶
        # 抵达前两个台阶，抵达前一个台阶，抵达当前台阶的方法数
        f_2, f_1, f = 0, 0, 1
        while current_step <= n:
            f_2 = f_1
            f_1 = f
            f = f_2 + f_1
            current_step += 1
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
