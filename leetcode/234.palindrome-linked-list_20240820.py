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
        list_nums = []
        cur_node = head
        while cur_node:
            list_nums.append(cur_node.val)
            cur_node = cur_node.next
        left = 0
        right = len(list_nums) - 1
        while left < right:
            if list_nums[left] != list_nums[right]:
                return False
            left, right = left + 1, right - 1
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
