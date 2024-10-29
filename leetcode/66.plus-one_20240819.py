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
        flag = 0
        for i in reversed(range(len(digits))):
            count = digits[i] + flag + 1 if i == len(digits) - 1 else digits[i] + flag
            if count > 9:
                digits[i] = count % 10
                flag = 1
            else:
                digits[i] = count
                flag = 0
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
