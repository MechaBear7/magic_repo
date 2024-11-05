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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur_head = dummy_head
        while list1 and list2:
            if list1.val < list2.val:
                cur_head.next = ListNode(list1.val)
                cur_head = cur_head.next
                list1 = list1.next
            else:
                cur_head.next = ListNode(list2.val)
                cur_head = cur_head.next
                list2 = list2.next
        rest_list = list1 if list1 else list2
        cur_head.next = rest_list
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
