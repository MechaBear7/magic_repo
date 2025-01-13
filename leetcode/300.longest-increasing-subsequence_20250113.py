"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-13 14:04:34
LastEditors: Helei.Yang
LastEditTime: 2025-01-13 14:21:42
FilePath: /magic_repo/leetcode/300.longest-increasing-subsequence_20250113.py
Description: 
"""

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
        # dp[i] 表示以 i 结尾的最大递增子序列的长度
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
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

