#
# @lc app=leetcode.cn id=94 lang=python3
# @lcpr version=30204
#
# [94] 二叉树的中序遍历
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(result, node):
            if not node:
                return
            dfs(result, node.left)
            result.append(node.val)
            dfs(result, node.right)

        result = []
        dfs(result, root)
        return result


# @lc code=end


#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
