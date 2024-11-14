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

        list_size = 0
        cur_node = dummy_head
        while cur_node and cur_node.next:
            cur_node = cur_node.next
            list_size += 1
        k %= list_size

        def reverse(head, start_idx, k):
            dummy_head = ListNode()
            dummy_head.next = head

            temp_head = dummy_head
            for _ in range(start_idx):
                temp_head = temp_head.next

            cnt = 0
            cur_node = temp_head.next
            while cur_node and cur_node.next and cnt < k:
                temp = cur_node.next.next
                cur_node.next.next = temp_head.next
                temp_head.next = cur_node.next
                cur_node.next = temp
                cnt += 1

            return dummy_head.next

        head = reverse(head, 0, list_size)
        head = reverse(head, 0, k - 1)
        head = reverse(head, k, list_size - k)

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
