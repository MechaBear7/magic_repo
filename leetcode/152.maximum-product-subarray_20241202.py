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
        max_dp = [0 for _ in range(len(nums))]
        min_dp = [0 for _ in range(len(nums))]
        max_dp[0], min_dp[0] = nums[0], nums[0]

        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i], nums[i])
            min_dp[i] = min(max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i], nums[i])

        return max(max_dp)


# @lc code=end


#
# @lcpr case=start
# [2,3,-2,4]\n
# @lcpr case=end

# @lcpr case=start
# [-2,0,-1]\n
# @lcpr case=end

#
