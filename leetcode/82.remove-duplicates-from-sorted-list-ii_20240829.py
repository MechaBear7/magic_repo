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
        while cur_node.next and cur_node.next.next:
            if cur_node.next.val == cur_node.next.next.val:
                temp_node = cur_node.next.next
                while temp_node and temp_node.val == cur_node.next.val:
                    temp_node = temp_node.next
                cur_node.next = temp_node
            else:
                cur_node = cur_node.next
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
