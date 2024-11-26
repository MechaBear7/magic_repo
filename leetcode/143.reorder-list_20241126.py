#
# @lc app=leetcode.cn id=143 lang=python3
# @lcpr version=30204
#
# [143] 重排链表
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy_head = ListNode()
        dummy_head.next = head
        slow, fast = dummy_head, dummy_head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp_head = slow
        cur_node = temp_head.next
        while cur_node and cur_node.next:
            temp = cur_node.next.next
            cur_node.next.next = temp_head.next
            temp_head.next = cur_node.next
            cur_node.next = temp
        n1, n2 = dummy_head.next, temp_head.next
        while n1 and n2:
            temp_head.next = None
            n1_next, n2_next = n1.next, n2.next
            n1.next = n2
            n2.next = n1_next
            n1, n2 = n1_next, n2_next


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#
