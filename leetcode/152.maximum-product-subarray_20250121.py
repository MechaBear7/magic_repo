"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-21 17:57:28
LastEditors: Helei.Yang
LastEditTime: 2025-01-21 17:59:46
FilePath: /magic_repo/leetcode/152.maximum-product-subarray_20250121.py
Description: 
"""

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
        n = len(nums)
        min_res = [0 for _ in range(n)]
        max_res = [0 for _ in range(n)]
        min_res[0], max_res[0] = nums[0], nums[0]
        for i in range(1, n):
            min_res[i] = min(min_res[i-1] * nums[i], max_res[i-1] * nums[i], nums[i])
            max_res[i] = max(min_res[i-1] * nums[i], max_res[i-1] * nums[i], nums[i])
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

