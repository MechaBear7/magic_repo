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
        if len(nums) < 2:
            return len(nums)
        n1, n2 = nums[0], nums[1]
        input_idx = 2
        search_idx = 2
        while search_idx < len(nums):
            n3 = nums[search_idx]
            while search_idx < len(nums) and n1 == n2 == n3:
                search_idx += 1
                if search_idx == len(nums):
                    return input_idx
                n3 = nums[search_idx]
            n1, n2, n3 = n2, n3, None
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
