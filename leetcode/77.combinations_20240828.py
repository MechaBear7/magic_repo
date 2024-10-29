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
        def backtracking(result, path, n, k, i):
            if len(path) == k:
                result.append(path[:])
                return
            if i > n:
                return
            # 选择当前数
            path.append(i)
            backtracking(result, path, n, k, i + 1)
            path.pop()
            # 不选择当前数
            backtracking(result, path, n, k, i + 1)

        result = []
        backtracking(result, [], n, k, 1)
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
