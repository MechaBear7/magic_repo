#
# @lc app=leetcode.cn id=112 lang=python3
# @lcpr version=30204
#
# [112] 路径总和
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # * DFS
        # if not root.left and not root.right:
        #     return root.val == targetSum
        # else:
        #     return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
        #         root.right, targetSum - root.val
        #     )

        # * 回溯

        # * BFS

        # * 栈
        # stack = [(root, root.val)]
        # while stack:
        #     node, cur_sum = stack.pop()
        #     if not node.left and not node.right and cur_sum == targetSum:
        #         return True
        #     if node.left:
        #         stack.append((node.left, cur_sum + node.left.val))
        #     if node.right:
        #         stack.append((node.right, cur_sum + node.right.val))
        # return False


# @lc code=end


#
# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,null,1]\n22\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#
