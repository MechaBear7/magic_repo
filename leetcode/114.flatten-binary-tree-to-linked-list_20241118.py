#
# @lc app=leetcode.cn id=114 lang=python3
# @lcpr version=30204
#
# [114] 二叉树展开为链表
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:  # 如果存在左子树
                search_node = root.left
                while search_node.right:  # 左子树的右子树找到最深
                    search_node = search_node.right
                search_node.right = root.right  # 将 root 的右子树挂到 search_node 上
                root.right = root.left  # 将 root 的左子树挂到右子树上
                root.left = None  # 清空 root 的左子树
            root = root.right  # 继续下一个节点的操作


# @lc code=end


#
# @lcpr case=start
# [1,2,5,3,4,null,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
