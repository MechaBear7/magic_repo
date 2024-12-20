#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30204
#
# [23] 合并 K 个升序链表
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(listnode1, listnode2):
            dummy_head = ListNode()
            cur_head = dummy_head
            n1, n2 = listnode1, listnode2
            while n1 and n2:
                if n1.val < n2.val:
                    cur_head.next = n1
                    n1 = n1.next
                else:
                    cur_head.next = n2
                    n2 = n2.next
                cur_head = cur_head.next
            cur_head.next = n1 or n2
            return dummy_head.next

        listnode = None
        for list_node in lists:
            listnode = merge(listnode, list_node)
        return listnode


# @lc code=end


#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#
