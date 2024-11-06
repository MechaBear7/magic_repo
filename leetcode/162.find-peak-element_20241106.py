#
# @lc app=leetcode.cn id=162 lang=python3
# @lcpr version=30204
#
# [162] 寻找峰值
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            left_num = -float("inf") if mid == 0 else nums[mid - 1]
            right_num = -float("inf") if mid == len(nums) - 1 else nums[mid + 1]
            if left_num < nums[mid] and nums[mid] > right_num:
                return mid
            elif left_num <= nums[mid] and nums[mid] <= right_num:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# @lc code=end


#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,3,5,6,4]\n
# @lcpr case=end

#
