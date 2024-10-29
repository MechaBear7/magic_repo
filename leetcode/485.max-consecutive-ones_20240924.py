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
        max_len = 0
        left = 0
        while left < len(nums):
            while left < len(nums) and nums[left] != 1:
                left += 1
            right = left
            while right < len(nums) and nums[right] == 1:
                right += 1
                max_len = max(max_len, right - left)
            left = right
        return max_len


# @lc code=end


#
# @lcpr case=start
# [1,1,0,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1,0,1]\n
# @lcpr case=end

#
