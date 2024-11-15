#
# @lc app=leetcode.cn id=24 lang=python3
# @lcpr version=30204
#
# [24] 两两交换链表中的节点
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head

        temp_head = dummy_head
        cur_node = temp_head.next
        while cur_node and cur_node.next:
            temp = cur_node.next.next
            cur_node.next.next = temp_head.next
            temp_head.next = cur_node.next
            cur_node.next = temp

            temp_head = temp_head.next.next
            cur_node = temp_head.next
        return dummy_head.next


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
