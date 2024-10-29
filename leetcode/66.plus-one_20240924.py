#
# @lc app=leetcode.cn id=66 lang=python3
# @lcpr version=30204
#
# [66] 加一
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 1
        for i in reversed(range(len(digits))):
            count = flag + digits[i]
            flag = count // 10
            digits[i] = count % 10
        if flag == 1:
            digits = [1] + digits
        return digits


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
