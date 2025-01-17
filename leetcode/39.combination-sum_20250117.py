"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-17 11:05:16
LastEditors: Helei.Yang
LastEditTime: 2025-01-17 11:13:34
FilePath: /magic_repo/leetcode/39.combination-sum_20250117.py
Description: 
"""

#
# @lc app=leetcode.cn id=39 lang=python3
# @lcpr version=30204
#
# [39] 组合总和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtracking(result, path, target, start_idx):
            if target == 0:
                result.append(path[:])
                return
            if start_idx >= len(candidates) or candidates[start_idx] > target:
                return
            # 使用当前值
            path.append(candidates[start_idx])
            backtracking(result, path, target - candidates[start_idx], start_idx)
            # 不使用当前值
            path.pop()
            backtracking(result, path, target, start_idx + 1)
        backtracking(result, [], target, 0)
        return result

# @lc code=end



#
# @lcpr case=start
# [2,3,6,7]\n7\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#

