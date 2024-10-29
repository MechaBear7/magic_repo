#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30204
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_symmetric(node1, node2):
            if not node1 and not node2:
                return True
            elif (node1 and not node2) or (not node1 and node2):
                return False
            elif node1.val != node2.val:
                return False
            else:
                return check_symmetric(node1.left, node2.right) and check_symmetric(
                    node1.right, node2.left
                )

        return check_symmetric(root.left, root.right)


# @lc code=end


#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#
