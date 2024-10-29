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
        while n != 1:
            if n in my_set:
                return False
            else:
                my_set.add(n)
                num = 0
                while n > 0:
                    num += (n % 10) * (n % 10)
                    n = n // 10
                n = num
        return True


# @lc code=end


#
# @lcpr case=start
# 19\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#
