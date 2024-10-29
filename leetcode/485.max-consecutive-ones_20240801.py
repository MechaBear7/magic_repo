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
        window_left = 0
        window_right = 0
        for idx in range(len(nums)):
            if nums[idx] != 1:
                max_length = max(max_length, window_right - window_left)
                window_left = idx
                window_right = idx
            else:
                window_right += 1
        max_length = max(max_length, window_right - window_left)
        return max_length

# @lc code=end



#
# @lcpr case=start
# [1,1,0,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1,0,1]\n
# @lcpr case=end

#

