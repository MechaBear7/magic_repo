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
        for idx, num in enumerate(nums):
            if num <= 0:
                nums[idx] = len(nums) + 1

        for idx, num in enumerate(nums):
            if abs(num) <= len(nums):
                nums[abs(num) - 1] = -abs(nums[abs(num) - 1])

        for idx, num in enumerate(nums):
            if num > 0:
                return idx + 1
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
