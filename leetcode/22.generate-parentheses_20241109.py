#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30204
#
# [22] 括号生成
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtracking(result, path, left, right):
            if left == right == 0:
                result.append("".join(path))
                return
            if left > 0:
                path.append("(")
                backtracking(result, path, left - 1, right)
                path.pop()
            if right > left:
                path.append(")")
                backtracking(result, path, left, right - 1)
                path.pop()
        result = []
        backtracking(result, [], n, n)
        return result
        
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

