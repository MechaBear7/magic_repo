"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-21 17:46:24
LastEditors: Helei.Yang
LastEditTime: 2025-01-21 17:56:56
FilePath: /magic_repo/leetcode/114.flatten-binary-tree-to-linked-list_20250121.py
Description: 
"""

#
# @lc app=leetcode.cn id=114 lang=python3
# @lcpr version=30204
#
# [114] 二叉树展开为链表
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur_node = root
        while cur_node:
            # 找到 cur_node 左节点的最右侧节点
            temp = cur_node.left
            if not temp:
                cur_node = cur_node.right
            else:
                while temp and temp.right:
                    temp = temp.right
                temp.right = cur_node.right
                cur_node.right = cur_node.left
                cur_node.left = None
                cur_node = cur_node.right
        
# @lc code=end



#
# @lcpr case=start
# [1,2,5,3,4,null,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

