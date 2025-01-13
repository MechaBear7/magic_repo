"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-13 13:31:21
LastEditors: Helei.Yang
LastEditTime: 2025-01-13 13:32:50
FilePath: /magic_repo/leetcode/102.binary-tree-level-order-traversal_20250113.py
Description: 
"""

#
# @lc app=leetcode.cn id=102 lang=python3
# @lcpr version=30204
#
# [102] 二叉树的层序遍历
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        cur_layer_nodes = [root]
        while cur_layer_nodes:
            cur_layer_values = []
            next_layer_nodes = []
            for node in cur_layer_nodes:
                cur_layer_values.append(node.val)
                if node.left:
                    next_layer_nodes.append(node.left)
                if node.right:
                    next_layer_nodes.append(node.right)
            result.append(cur_layer_values)
            cur_layer_nodes = next_layer_nodes
        return result

# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

