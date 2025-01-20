"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-20 17:09:16
LastEditors: Helei.Yang
LastEditTime: 2025-01-20 17:28:11
FilePath: /magic_repo/leetcode/78.subsets_20250120.py
Description: 
"""

#
# @lc app=leetcode.cn id=78 lang=python3
# @lcpr version=30204
#
# [78] 子集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(result, path, nums, idx, cnt):
            if len(path) == cnt:
                result.append(path[:])
                return
            if idx >= len(nums):
                return
            path.append(nums[idx])
            dfs(result, path, nums, idx + 1, cnt)
            path.pop()
            dfs(result, path, nums, idx + 1, cnt)

        result = [[]]
        for i in range(1, len(nums) + 1):
            dfs(result, [], nums, 0, i)
        return result

# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

