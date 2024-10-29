#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30204
#
# [2] 两数相加
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
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1_node = l1
        l2_node = l2

        dummy_head = ListNode()
        cur_node = dummy_head

        tmp = 0
        while l1_node and l2_node:
            count = l1_node.val + l2_node.val + tmp
            tmp = int(count / 10)
            cur_node.next = ListNode(count % 10)
            cur_node = cur_node.next
            l1_node = l1_node.next
            l2_node = l2_node.next

        node = l1_node if l1_node else l2_node
        while node:
            count = node.val + tmp
            tmp = int(count / 10)
            cur_node.next = ListNode(count % 10)
            cur_node = cur_node.next
            node = node.next

        if tmp == 1:
            cur_node.next = ListNode(1)

        return dummy_head.next


# @lc code=end


#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#
