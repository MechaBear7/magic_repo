#
# @lc app=leetcode.cn id=142 lang=python3
# @lcpr version=30204
#
# [142] 环形链表 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head

        slow_node, fast_node = dummy_head, dummy_head

        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

            if slow_node == fast_node:
                n1, n2 = dummy_head, slow_node
                while n1 != n2:
                    n1, n2 = n1.next, n2.next
                return n1

        return None


# @lc code=end


#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#
