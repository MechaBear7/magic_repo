#
# @lc app=leetcode.cn id=206 lang=python3
# @lcpr version=30204
#
# [206] 反转链表
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head

        cur_head = dummy_head.next
        while cur_head and cur_head.next:
            next_head = cur_head.next
            cur_head.next = next_head.next
            next_head.next = dummy_head.next
            dummy_head.next = next_head

        return dummy_head.next


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
