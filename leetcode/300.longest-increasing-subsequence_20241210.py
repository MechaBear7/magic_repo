#
# @lc app=leetcode.cn id=300 lang=python3
# @lcpr version=30204
#
# [300] 最长递增子序列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        for idx in range(n):
            max_incre = 0
            for jdx in range(idx):
                if nums[idx] > nums[jdx]:
                    max_incre = max(max_incre, dp[jdx])
            dp[idx] = max_incre + 1
        return max(dp)


# @lc code=end


#
# @lcpr case=start
# [10,9,2,5,3,7,101,18]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

#
