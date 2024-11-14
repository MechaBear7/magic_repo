#
# @lc app=leetcode.cn id=230 lang=python3
# @lcpr version=30204
#
# [230] 二叉搜索树中第K小的元素
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 1
        stack = []
        cur_node = root
        while stack or cur_node:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            if cnt == k:
                return cur_node.val
            cur_node = cur_node.right
            cnt += 1


# @lc code=end


#
# @lcpr case=start
# [3,1,4,null,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,null,1]\n3\n
# @lcpr case=end

#
