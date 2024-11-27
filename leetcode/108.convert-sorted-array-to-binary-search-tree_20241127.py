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
        def construct_node(nums):
            if len(nums) == 0:
                return None
            left, right = 0, len(nums) - 1
            mid = left + (right - left) // 2
            cur_node = TreeNode(nums[mid])
            cur_node.left = construct_node(nums[left:mid])
            cur_node.right = construct_node(nums[mid + 1 : right + 1])
            return cur_node

        return construct_node(nums)


# @lc code=end


#
# @lcpr case=start
# [-10,-3,0,5,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n
# @lcpr case=end

#
