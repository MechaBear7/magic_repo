#
# @lc app=leetcode.cn id=86 lang=python3
# @lcpr version=30204
#
# [86] 分隔链表
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_1, dummy_2 = ListNode(), ListNode()
        n1, n2 = dummy_1, dummy_2

        cur_node = head
        while cur_node:
            if cur_node.val < x:
                n1.next = cur_node
                n1 = n1.next
            else:
                n2.next = cur_node
                n2 = n2.next
            cur_node = cur_node.next

        n1.next = dummy_2.next
        n2.next = None
        return dummy_1.next


# @lc code=end


#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#
