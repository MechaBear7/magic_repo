#
# @lc app=leetcode.cn id=18 lang=python3
# @lcpr version=30204
#
# [18] 四数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        for idx in range(len(nums) - 3):
            if idx != 0 and nums[idx] == nums[idx - 1]:
                continue
            for jdx in range(idx + 1, len(nums) - 2):
                if jdx != idx + 1 and nums[jdx] == nums[jdx - 1]:
                    continue

# @lc code=end



#
# @lcpr case=start
# [1,0,-1,0,-2,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n8\n
# @lcpr case=end

#

