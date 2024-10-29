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
        def backtracking(result, n, k, start_idx, path):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start_idx, n + 1):
                path.append(i)
                backtracking(result, n, k, i + 1, path)  # 只会选择 i + 1 节点后的
                path.pop()

        result = []
        backtracking(result, n, k, 1, [])
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
