#
# @lc app=leetcode.cn id=103 lang=python3
# @lcpr version=30204
#
# [103] 二叉树的锯齿形层序遍历
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        reverse = False
        cur_nodes = [root]
        while cur_nodes:
            cur_layer_result = []
            next_layer_nodes = []
            for node in cur_nodes:
                cur_layer_result.append(node.val)
                if node.left:
                    next_layer_nodes.append(node.left)
                if node.right:
                    next_layer_nodes.append(node.right)
            if reverse:
                result.append(list(reversed(cur_layer_result)))
            else:
                result.append(cur_layer_result)
            cur_nodes = next_layer_nodes
            reverse = not reverse
        return result

# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

