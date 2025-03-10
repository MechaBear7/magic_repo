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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur_head = dummy_head
        flag = 0
        n1, n2 = l1, l2
        while n1 and n2:
            val = flag + n1.val + n2.val
            cur_head.next = ListNode(val % 10)
            flag = val // 10
            cur_head = cur_head.next
            n1, n2 = n1.next, n2.next
        node = n1 if n1 else n2
        while node:
            val = flag + node.val
            cur_head.next = ListNode(val % 10)
            flag = val // 10
            cur_head = cur_head.next
            node = node.next
        if flag == 1:
            cur_head.next = ListNode(1)
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

