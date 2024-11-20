#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30204
#
# [23] 合并 K 个升序链表
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur_node = dummy_head
        cur_nodes = [node for node in lists]
        while True:
            min_idx = -1
            min_value = float("inf")
            for idx, node in enumerate(cur_nodes):
                if node and node.val < min_value:
                    min_idx = idx
                    min_value = node.val
            if min_idx == -1:
                break
            cur_node.next = ListNode(min_value)
            cur_node = cur_node.next
            cur_nodes[min_idx] = cur_nodes[min_idx].next
        return dummy_head.next


# @lc code=end


#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#
