#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30204
#
# [283] 移动零
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        input_idx = 0
        for search_idx in range(len(nums)):
            if nums[search_idx] != 0:
                nums[input_idx] = nums[search_idx]
                input_idx += 1
        for i in range(input_idx, len(nums)):
            nums[i] = 0


# @lc code=end


#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
