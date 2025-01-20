"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-20 18:00:13
LastEditors: Helei.Yang
LastEditTime: 2025-01-20 18:01:41
FilePath: /magic_repo/leetcode/LCR 145.判断对称二叉树_20250120.py
Description: 
"""

#
# @lc app=leetcode.cn id=LCR 145 lang=python3
# @lcpr version=30204
#
# [LCR 145] 判断对称二叉树
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
    def checkSymmetricTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check_nodes(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 and node2 or node1 and not node2:
                return False
            elif node1.val != node2.val:
                return False
            else:
                return check_nodes(node1.left, node2.right) and check_nodes(node1.right, node2.left)
        
        return check_nodes(root.left, root.right)
# @lc code=end



#
# @lcpr case=start
# [6,7,7,8,9,9,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#

