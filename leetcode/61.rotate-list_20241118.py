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
        if not head:
            return None

        dummy_head = ListNode()
        dummy_head.next = head

        def reverse(head, start, end):
            dummy_head = ListNode()
            dummy_head.next = head

            temp_head = dummy_head
            for _ in range(start):
                temp_head = temp_head.next

            cnt = 1
            cur_node = temp_head.next
            while cur_node and cur_node.next and start + cnt < end:
                temp = cur_node.next.next
                cur_node.next.next = temp_head.next
                temp_head.next = cur_node.next
                cur_node.next = temp
                cnt += 1

            return dummy_head.next

        list_len = 0
        cur_node = dummy_head.next
        while cur_node:
            list_len += 1
            cur_node = cur_node.next
        k = k % list_len
        head = reverse(head, 0, list_len)
        head = reverse(head, 0, k)
        head = reverse(head, k, list_len)

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
