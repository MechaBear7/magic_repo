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
        slow_node, fast_node = head, head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if slow_node == fast_node:
                entry = head
                while entry != slow_node:
                    entry = entry.next
                    slow_node = slow_node.next
                return entry
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
