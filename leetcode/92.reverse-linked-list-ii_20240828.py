#
# @lc app=leetcode.cn id=92 lang=python3
# @lcpr version=30204
#
# [92] 反转链表 II
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
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        reversed_start_node = dummy_head
        for _ in range(left - 1):
            reversed_start_node = reversed_start_node.next
        cur_node = reversed_start_node.next
        for _ in range(right - left):
            temp = cur_node.next.next
            cur_node.next.next = reversed_start_node.next
            reversed_start_node.next = cur_node.next
            cur_node.next = temp
        return dummy_head.next


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

#
