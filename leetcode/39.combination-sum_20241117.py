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

        def backtracking(result, path, candidates, target, idx):
            if target == 0:
                result.append(path[:])
                return
            if candidates[idx] > target:
                return
            for cnt_idx in range(idx, len(candidates)):
                path.append(candidates[cnt_idx])
                backtracking(result, path, candidates, target - candidates[cnt_idx], cnt_idx)
                path.pop()

        result = []
        backtracking(result, [], candidates, target, 0)

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
