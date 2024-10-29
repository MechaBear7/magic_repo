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
        dummy_head = ListNode()
        cur_node = dummy_head
        flag = 0
        while l1 and l2:
            count = l1.val + l2.val + flag
            flag = 1 if count > 9 else 0
            cur_node.next = ListNode(count % 10)
            cur_node = cur_node.next
            l1 = l1.next
            l2 = l2.next
        node = l1 if l1 else l2
        while node:
            count = node.val + flag
            flag = 1 if count > 9 else 0
            cur_node.next = ListNode(count % 10)
            cur_node = cur_node.next
            node = node.next
        if flag == 1:
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
