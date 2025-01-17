"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-17 14:05:26
LastEditors: Helei.Yang
LastEditTime: 2025-01-17 14:18:09
FilePath: /magic_repo/leetcode/61.rotate-list_20250117.py
Description: 
"""

#
# @lc app=leetcode.cn id=61 lang=python3
# @lcpr version=30204
#
# [61] 旋转链表
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy_head = ListNode()
        dummy_head.next = head
        # 统计总共多少个节点
        cur_node = dummy_head.next
        cnts = 0
        while cur_node:
            cnts += 1
            cur_node = cur_node.next
        k = k % cnts

        def reverse(head, start, k):
            dummy_head = ListNode()
            dummy_head.next = head
            temp_head = dummy_head
            for _ in range(start):
                temp_head = temp_head.next
            cur_node = temp_head.next
            for _ in range(k - 1):
                temp = cur_node.next.next
                cur_node.next.next = temp_head.next
                temp_head.next = cur_node.next
                cur_node.next = temp
            return dummy_head.next

        head = reverse(head, 0, cnts)
        head = reverse(head, 0, k)
        head = reverse(head, k, cnts - k)

        return head

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2]\n4\n
# @lcpr case=end

#

