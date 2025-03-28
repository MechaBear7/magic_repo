#
# @lc app=leetcode.cn id=198 lang=python3
# @lcpr version=30204
#
# [198] 打家劫舍
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        # dp[i] 表示打劫前 i 个房屋可以获得的利润
        dp = [0 for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i - 1], nums[i])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]


# @lc code=end


#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#
