#
# @lc app=leetcode.cn id=485 lang=python3
# @lcpr version=30204
#
# [485] 最大连续 1 的个数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        left_window = 0
        right_window = 0
        for idx, num in enumerate(nums):
            if num != 1:
                max_length = max(max_length, right_window - left_window)
                left_window = idx
                right_window = idx
            else:
                right_window += 1
        return max(max_length, right_window - left_window)
# @lc code=end



#
# @lcpr case=start
# [1,1,0,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1,0,1]\n
# @lcpr case=end

#

