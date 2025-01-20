"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-20 18:13:24
LastEditors: Helei.Yang
LastEditTime: 2025-01-20 18:15:54
FilePath: /magic_repo/leetcode/86.partition-list_20250120.py
Description: 
"""

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
        dummy_head1 = ListNode()
        dummy_head2 = ListNode()
        n1, n2 = dummy_head1, dummy_head2
        cur_node = head
        while cur_node:
            if cur_node.val < x:
                n1.next = ListNode(cur_node.val)
                n1 = n1.next
            else:
                n2.next = ListNode(cur_node.val)
                n2 = n2.next
            cur_node = cur_node.next
        n1.next = dummy_head2.next
        return dummy_head1.next
# @lc code=end



#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#

