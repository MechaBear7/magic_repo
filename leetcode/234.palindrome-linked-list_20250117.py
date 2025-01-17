"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-17 10:49:58
LastEditors: Helei.Yang
LastEditTime: 2025-01-17 10:57:14
FilePath: /magic_repo/leetcode/234.palindrome-linked-list_20250117.py
Description: 
"""

#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30204
#
# [234] 回文链表
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy_head = ListNode()
        dummy_head.next = head
        slow, fast = dummy_head, dummy_head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp_head = slow
        cur_node = temp_head.next
        while cur_node and cur_node.next:
            temp = cur_node.next.next
            cur_node.next.next = temp_head.next
            temp_head.next = cur_node.next
            cur_node.next = temp
        n1, n2 = dummy_head.next, temp_head.next
        while n1 and n2:
            if n1.val != n2.val:
                return False
            n1, n2 = n1.next, n2.next
        return True

    
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

