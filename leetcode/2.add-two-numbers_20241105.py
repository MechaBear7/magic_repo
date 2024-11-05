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
        self.dummy_head = ListNode()
        cur_node = self.dummy_head
        flag = 0
        while l1 and l2:
            num = flag + l1.val + l2.val
            if num > 9:
                flag = 1
            else:
                flag = 0
            new_node = ListNode(num % 10)
            cur_node.next = new_node
            cur_node = cur_node.next
            l1, l2 = l1.next, l2.next
        node = l1 if l1 else l2
        while node:
            num = flag + node.val
            if num > 9:
                flag = 1
            else:
                flag = 0
            new_node = ListNode(num % 10)
            cur_node.next = new_node
            cur_node = cur_node.next
            node = node.next
        if flag == 1:
            cur_node.next = ListNode(1)
        return self.dummy_head.next


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
