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
        for idx in reversed(range(len(digits))):
            if digits[idx] + 1 <= 9:
                digits[idx] += 1
                return digits
            digits[idx] = 0
        return [1] + digits
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

