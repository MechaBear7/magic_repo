#
# @lc app=leetcode.cn id=83 lang=python3
# @lcpr version=30204
#
# [83] 删除排序链表中的重复元素
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
        if not head:
            return head
        dummy_head = ListNode()
        dummy_head.next = head
        cur_node = dummy_head.next
        search_node = cur_node.next
        while cur_node:
            if search_node is None:
                cur_node.next = search_node
                cur_node = cur_node.next
            elif cur_node.val == search_node.val:
                search_node = search_node.next
            else:
                cur_node.next = search_node
                cur_node = cur_node.next
                search_node = search_node.next
        return dummy_head.next


# @lc code=end


#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,3]\n
# @lcpr case=end

#
