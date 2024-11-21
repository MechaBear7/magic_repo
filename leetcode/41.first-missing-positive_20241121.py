#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30204
#
# [41] 缺失的第一个正数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            if nums[idx] <= 0:
                nums[idx] = len(nums) + 1
        for idx in range(len(nums)):
            if abs(nums[idx]) <= len(nums):
                nums[abs(nums[idx]) - 1] = -abs(nums[abs(nums[idx]) - 1])
        print(nums)
        for i in range(0, len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1


# @lc code=end


#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#
