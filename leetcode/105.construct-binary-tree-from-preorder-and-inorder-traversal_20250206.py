"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-02-06 10:37:03
LastEditors: Helei.Yang
LastEditTime: 2025-02-06 10:39:35
FilePath: /magic_repo/leetcode/105.construct-binary-tree-from-preorder-and-inorder-traversal_20250206.py
Description: 
"""

#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30204
#
# [105] 从前序与中序遍历序列构造二叉树
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for idx, val in enumerate(inorder):
            hashmap[val] = idx
        
        def construct_node(i, left, right):
            if right < left:
                return None
            cur_node = TreeNode(preorder[i])
            idx = hashmap[preorder[i]]
            cur_node.left = construct_node(i + 1, left, idx - 1)
            cur_node.right = construct_node(i + idx - left + 1, idx + 1, right)
            return cur_node
        
        return construct_node(0, 0, len(inorder) - 1)

# @lc code=end



#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#

