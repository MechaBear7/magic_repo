#
# @lc app=leetcode.cn id=82 lang=python3
# @lcpr version=30204
#
# [82] 删除排序链表中的重复元素 II
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        cur_node = dummy_head
        next_node = cur_node.next
        while next_node and next_node.next:
            if next_node.val == next_node.next.val:
                node = next_node
                while node and node.val == next_node.val:
                    node = node.next
                cur_node.next = node
            else:
                cur_node = cur_node.next
            next_node = cur_node.next

        return dummy_head.next


# @lc code=end


#
# @lcpr case=start
# [1,2,3,3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2,3]\n
# @lcpr case=end

#
