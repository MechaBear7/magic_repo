#
# @lc app=leetcode.cn id=129 lang=python3
# @lcpr version=30204
#
# [129] 求根节点到叶节点数字之和
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        def backtracking(path, node):
            nonlocal result
            path = path * 10 + node.val
            if not node.left and not node.right:
                result += path
                return
            if node.left:
                backtracking(path, node.left)
            if node.right:
                backtracking(path, node.right)

        backtracking(0, root)
        return result


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,0,5,1]\n
# @lcpr case=end

#
