"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-13 13:33:35
LastEditors: Helei.Yang
LastEditTime: 2025-01-13 13:54:56
FilePath: /magic_repo/leetcode/129.sum-root-to-leaf-numbers_20250113.py
Description: 
"""

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
        def backtracking(path, node):
            nonlocal result
            if not node:
                return
            path += node.val
            if not node.left and not node.right:
                result += path
            else:
                backtracking(path * 10, node.left)
                backtracking(path * 10, node.right)
        result = 0
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

