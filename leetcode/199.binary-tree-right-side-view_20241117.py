#
# @lc app=leetcode.cn id=199 lang=python3
# @lcpr version=30204
#
# [199] 二叉树的右视图
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        layer_nodes = [root]
        while layer_nodes:
            cur_layer_result = []
            new_layer_nodes = []
            for node in layer_nodes:
                cur_layer_result.append(node.val)
                if node.left:
                    new_layer_nodes.append(node.left)
                if node.right:
                    new_layer_nodes.append(node.right)
            result.append(cur_layer_result[-1])
            layer_nodes = new_layer_nodes
        return result


# @lc code=end


#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
