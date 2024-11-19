#
# @lc app=leetcode.cn id=LCR 174 lang=python3
# @lcpr version=30204
#
# [LCR 174] 寻找二叉搜索树中的目标节点
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
    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        stk = []
        cur_node = root
        k = 1
        while stk or cur_node:
            while cur_node:
                stk.append(cur_node)
                cur_node = cur_node.right
            cur_node = stk.pop()
            if k == cnt:
                return cur_node.val
            k += 1
            cur_node = cur_node.left


# @lc code=end


#
# @lcpr case=start
# [7, 3, 9, 1, 5]\n27/ \3   9/ \1   5\n
# @lcpr case=end

# @lcpr case=start
# [10, 5, 15, 2, 7, null, 20, 1, null, 6, 8]\n410/ \5   15/ \    \2   7    20/   / \ 1   6   8\n
# @lcpr case=end

#
