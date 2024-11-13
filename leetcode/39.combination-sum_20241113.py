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
        def dfs(i: int, s: int):
            if s == 0:
                result.append(path[:])
                return
            if s < candidates[i]:
                return
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                dfs(j, s - candidates[j])
                path.pop()

        candidates.sort()
        result = []
        path = []
        dfs(0, target)
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
