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
        dummy_head = ListNode()
        dummy_head.next = head
        cur_node = dummy_head.next
        while cur_node and cur_node.next:
            if cur_node.val == cur_node.next.val:
                temp = cur_node.next
                while temp and temp.val == cur_node.val:
                    temp = temp.next
                cur_node.next = temp
            else:
                cur_node = cur_node.next

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
