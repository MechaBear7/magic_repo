#
# @lc app=leetcode.cn id=26 lang=python3
# @lcpr version=30204
#
# [26] 删除有序数组中的重复项
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, input_idx = 0, 0
        while i < len(nums):
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            nums[input_idx] = nums[i]
            i, input_idx = i + 1, input_idx + 1
        return input_idx


# @lc code=end


#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#
