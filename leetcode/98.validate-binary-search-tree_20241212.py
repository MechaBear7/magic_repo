#
# @lc app=leetcode.cn id=98 lang=python3
# @lcpr version=30204
#
# [98] 验证二叉搜索树
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre_num = -float("inf")
        stk = []
        cur_node = root
        while stk or cur_node:
            while cur_node:
                stk.append(cur_node)
                cur_node = cur_node.left
            cur_node = stk.pop()
            if pre_num >= cur_node.val:
                return False
            pre_num = cur_node.val
            cur_node = cur_node.right
        return True


# @lc code=end


#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,null,null,3,6]\n
# @lcpr case=end

#
