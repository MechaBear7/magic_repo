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
        my_set = set()
        input_idx = 0
        for search_idx in range(len(nums)):
            if nums[search_idx] not in my_set:
                nums[input_idx] = nums[search_idx]
                my_set.add(nums[search_idx])
                input_idx += 1
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
