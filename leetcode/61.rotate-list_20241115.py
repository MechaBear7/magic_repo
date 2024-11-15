#
# @lc app=leetcode.cn id=61 lang=python3
# @lcpr version=30204
#
# [61] 旋转链表
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, start, end):
            dummy_head = ListNode()
            dummy_head.next = head

            temp_head = dummy_head
            for i in range(start):
                temp_head = temp_head.next

            cur_node = temp_head.next
            for i in range(end - start):
                temp = cur_node.next.next
                cur_node.next.next = temp_head.next
                temp_head.next = cur_node.next
                cur_node.next = temp

            return dummy_head.next

        if not head:
            return None
        total_len = 0
        cur_head = head
        while cur_head:
            total_len += 1
            cur_head = cur_head.next
        k = k % total_len
        head = reverse(head, 0, total_len - 1)
        head = reverse(head, 0, k - 1)
        head = reverse(head, k, total_len - 1)

        return head


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2]\n4\n
# @lcpr case=end

#
