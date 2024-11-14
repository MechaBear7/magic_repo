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
        candidates = sorted(candidates)

        def dfs(result, path, nums, target, start_idx):
            if target == 0:
                result.append(path[:])
                return
            if target < nums[start_idx]:
                return
            for idx in range(start_idx, len(nums)):
                path.append(nums[idx])
                dfs(result, path, nums, target - nums[idx], idx)
                path.pop()

        result, path = [], []
        for i in range(len(candidates)):
            path.append(candidates[i])
            dfs(result, path, candidates, target - candidates[i], i)
            path.pop()
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
