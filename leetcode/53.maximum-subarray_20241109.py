#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30204
#
# [53] 最大子数组和
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] 表示以 i 结尾的最大连续子数组和
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
        return max(dp)


# @lc code=end


#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#
