#
# @lc app=leetcode.cn id=530 lang=python3
# @lcpr version=30204
#
# [530] 二叉搜索树的最小绝对差
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        pre_num = -float("inf")
        min_diff = float("inf")
        stack = []
        node = root
        while node or stack:  # 如果 node 和 stack 全都是空的，说明全查完了
            while node:  # 将当前节点的所有左节点入栈
                stack.append(node)
                node = node.left
            # 输出栈顶的节点值，然后从它右边的子节点继续。
            node = stack.pop()
            min_diff = min(min_diff, node.val - pre_num)
            pre_num = node.val
            node = node.right
        return min_diff


# @lc code=end


#
# @lcpr case=start
# [4,2,6,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,48,null,null,12,49]\n
# @lcpr case=end

#
