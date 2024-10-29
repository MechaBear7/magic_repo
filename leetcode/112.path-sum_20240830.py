#
# @lc app=leetcode.cn id=112 lang=python3
# @lcpr version=30204
#
# [112] 路径总和
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # 如果当前节点是叶子结点
        if not root.left and not root.right:
            return True if root.val == targetSum else False

        left_node_result, right_node_result = False, False
        if root.left:  # 如果有左节点
            left_node_result = self.hasPathSum(root.left, targetSum - root.val)
        if root.right:  # 如果有右节点
            right_node_result = self.hasPathSum(root.right, targetSum - root.val)

        return left_node_result or right_node_result


# @lc code=end


#
# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,null,1]\n22\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#
