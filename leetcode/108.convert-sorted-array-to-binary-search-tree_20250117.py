"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-17 11:26:11
LastEditors: Helei.Yang
LastEditTime: 2025-01-17 11:28:26
FilePath: /magic_repo/leetcode/108.convert-sorted-array-to-binary-search-tree_20250117.py
Description: 
"""

#
# @lc app=leetcode.cn id=108 lang=python3
# @lcpr version=30204
#
# [108] 将有序数组转换为二叉搜索树
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct_sub_tree(nums):
            if len(nums) == 0:
                return None
            left, right = 0, len(nums) - 1
            mid = left + (right - left) // 2
            cur_node = TreeNode(val=nums[mid])
            cur_node.left = construct_sub_tree(nums[:mid])
            cur_node.right = construct_sub_tree(nums[mid+1:])
            return cur_node
        root = construct_sub_tree(nums)
        return root

# @lc code=end



#
# @lcpr case=start
# [-10,-3,0,5,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n
# @lcpr case=end

#

