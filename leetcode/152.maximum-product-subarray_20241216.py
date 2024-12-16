#
# @lc app=leetcode.cn id=152 lang=python3
# @lcpr version=30204
#
# [152] 乘积最大子数组
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_res = [0 for _ in range(len(nums))]
        max_res = [0 for _ in range(len(nums))]
        min_res[0], max_res[0] = nums[0], nums[0]
        for idx in range(1, len(nums)):
            min_res[idx] = min(min_res[idx - 1] * nums[idx], max_res[idx - 1] * nums[idx], nums[idx])
            max_res[idx] = max(min_res[idx - 1] * nums[idx], max_res[idx - 1] * nums[idx], nums[idx])
        return max(max_res)


# @lc code=end


#
# @lcpr case=start
# [2,3,-2,4]\n
# @lcpr case=end

# @lcpr case=start
# [-2,0,-1]\n
# @lcpr case=end

#
