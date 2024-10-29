#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30204
#
# [19] 删除链表的倒数第 N 个结点
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        slow_node, fast_node = dummy_head, dummy_head
        # 将 fast_node 向后移 n 个节点
        for _ in range(n):
            fast_node = fast_node.next
        # slow_node 和 fast_node 共同后移
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next
        slow_node.next = slow_node.next.next
        return dummy_head.next

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

