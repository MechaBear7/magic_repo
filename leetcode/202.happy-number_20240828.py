#
# @lc app=leetcode.cn id=202 lang=python3
# @lcpr version=30204
#
# [202] 快乐数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        my_set = set()
        while n not in my_set:
            my_set.add(n)
            new_n = 0
            while n > 0:
                num = n % 10
                new_n += num * num
                n = n // 10
            if new_n == 1:
                return True
            n = new_n
        return False


# @lc code=end


#
# @lcpr case=start
# 19\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#
