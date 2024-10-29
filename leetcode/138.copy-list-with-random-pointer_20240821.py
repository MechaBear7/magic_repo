#
# @lc app=leetcode.cn id=138 lang=python3
# @lcpr version=30204
#
# [138] 随机链表的复制
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        map_dict = {None: None}
        # 构建原节点与新节点的关系映射
        cur_node = head
        while cur_node:
            map_dict[cur_node] = Node(cur_node.val)
            cur_node = cur_node.next
        # 构建原节点与新节点的 next 关系映射
        cur_node = head
        while cur_node:
            map_dict[cur_node].next = map_dict[cur_node.next]
            cur_node = cur_node.next
        # 构建原节点与新节点的 random 关系映射
        cur_node = head
        while cur_node:
            map_dict[cur_node].random = map_dict[cur_node.random]
            cur_node = cur_node.next
        return map_dict[head]


# @lc code=end


#
# @lcpr case=start
# [[7,null],[13,0],[11,4],[10,2],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,null],[3,0],[3,null]]\n
# @lcpr case=end

#
