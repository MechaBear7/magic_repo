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
        def backtracking(result, path, target, candidates, start_idx):
            if target == 0:
                result.append(path[:])
                return
            if start_idx == len(candidates) or candidates[start_idx] > target:
                return
            for idx in range(start_idx, len(candidates)):
                path.append(candidates[idx])
                backtracking(result, path, target - candidates[idx], candidates, idx)
                path.pop()

        candidates.sort()
        result = []
        backtracking(result, [], target, candidates, 0)
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
