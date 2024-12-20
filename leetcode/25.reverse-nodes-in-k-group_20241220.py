#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30204
#
# [25] K 个一组翻转链表
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnts = 0
        cur_node = head
        while cur_node:
            cnts += 1
            cur_node = cur_node.next
        reverse_cnts = cnts // k

        def reverse(head, start, k):
            dummy_head = ListNode()
            dummy_head.next = head
            temp_head = dummy_head
            for _ in range(start):
                temp_head = temp_head.next
            cur_node = temp_head.next
            for _ in range(k - 1):
                temp = cur_node.next.next
                cur_node.next.next = temp_head.next
                temp_head.next = cur_node.next
                cur_node.next = temp
            return dummy_head.next

        for i in range(reverse_cnts):
            head = reverse(head, i * k, k)

        return head


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#
