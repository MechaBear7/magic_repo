#
# @lc app=leetcode.cn id=77 lang=python3
# @lcpr version=30204
#
# [77] 组合
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(result, path, idx):
            if len(path) == k:
                result.append(path[:])
                return
            if idx > n:
                return
            path.append(idx)
            backtracking(result, path, idx + 1)
            path.pop()
            backtracking(result, path, idx + 1)

        result = []
        backtracking(result, [], 1)
        return result


# @lc code=end


#
# @lcpr case=start
# 4\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#
