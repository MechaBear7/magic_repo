#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30204
#
# [21] 合并两个有序链表
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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur_node = dummy_head

        while list1 and list2:
            if list1.val < list2.val:
                cur_node.next = ListNode(list1.val)
                cur_node, list1 = cur_node.next, list1.next
            else:
                cur_node.next = ListNode(list2.val)
                cur_node, list2 = cur_node.next, list2.next
        cur_node.next = list1 if list1 else list2

        return dummy_head.next


# @lc code=end


#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#
