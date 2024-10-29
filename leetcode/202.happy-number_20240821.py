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
        num = n
        my_set = set()
        while True:
            if num == 1:
                break
            new_num = 0
            while num > 0:
                new_num += (num % 10) * (num % 10)
                num = num // 10
            if new_num in my_set:
                return False
            else:
                my_set.add(new_num)
                num = new_num
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
