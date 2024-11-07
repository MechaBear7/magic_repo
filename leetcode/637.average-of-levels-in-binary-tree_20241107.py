#
# @lc app=leetcode.cn id=637 lang=python3
# @lcpr version=30204
#
# [637] 二叉树的层平均值
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if not root:
            return result

        layer_nodes = [root]
        while layer_nodes:
            next_layer = []
            layer_sum = 0
            for node in layer_nodes:
                layer_sum += node.val
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            result.append(layer_sum / len(layer_nodes))
            layer_nodes = next_layer
        return result


# @lc code=end


#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [3,9,20,15,7]\n
# @lcpr case=end

#
