#
# @lc app=leetcode.cn id=236 lang=python3
# @lcpr version=30204
#
# [236] 二叉树的最近公共祖先
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        def has_child(node, n1, n2):
            if node in (None, n1, n2):
                return node
            left_has_child = has_child(node.left, n1, n2)
            right_has_child = has_child(node.right, n1, n2)

            if left_has_child and right_has_child:
                return node
            return left_has_child or right_has_child

        return has_child(root, p, q)


# @lc code=end


#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n2\n
# @lcpr case=end

#
