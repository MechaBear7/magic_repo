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
            pivot = left + (right - left)
            left_num = nums[pivot - 1] if pivot - 1 >= 0 else -float("inf")
            cur_num = nums[pivot]
            right_num = nums[pivot + 1] if pivot + 1 < len(nums) else -float("inf")
            if left_num < cur_num and cur_num > right_num:
                return pivot
            elif left_num < cur_num < right_num:
                left = pivot + 1
            else:
                right = pivot - 1
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
