#
# @lc app=leetcode.cn id=80 lang=python3
# @lcpr version=30204
#
# [80] 删除有序数组中的重复项 II
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        input_idx = 0
        search_idx = 0
        while search_idx < len(nums):
            while (
                0 <= search_idx - 1
                and search_idx + 1 < len(nums)
                and nums[search_idx - 1] == nums[search_idx] == nums[search_idx + 1]
            ):
                search_idx += 1
            nums[input_idx] = nums[search_idx]
            input_idx += 1
            search_idx += 1

        return input_idx


# @lc code=end


#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#
