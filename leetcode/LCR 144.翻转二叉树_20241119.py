#
# @lc app=leetcode.cn id=LCR 144 lang=python3
# @lcpr version=30204
#
# [LCR 144] 翻转二叉树
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
    def flipTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.flipTree(root.left)
        self.flipTree(root.right)
        return root


# @lc code=end


#
# @lcpr case=start
# [5,7,9,8,3,2,4]\n
# @lcpr case=end

#
