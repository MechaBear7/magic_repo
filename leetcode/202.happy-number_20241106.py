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
        num = n
        while True:
            new_num = 0
            while num > 0:
                c = num % 10
                new_num += c * c
                num = num // 10
            if new_num in my_set:
                break
            elif new_num == 1:
                return True
            else:
                my_set.add(new_num)
                num = new_num
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
