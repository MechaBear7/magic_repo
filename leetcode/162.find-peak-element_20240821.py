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
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            left_num = nums[mid - 1] if mid - 1 >= 0 else -float("inf")
            cur_num = nums[mid]
            right_num = nums[mid + 1] if mid + 1 < len(nums) else -float("inf")

            if left_num < cur_num and cur_num > right_num:
                return mid
            elif left_num < cur_num < right_num:
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
