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
        if len(lists) == 0:
            return None

        def merge_list(list1, list2):
            dummy_head = ListNode()
            cur_node = dummy_head
            n1, n2 = list1, list2

            while n1 and n2:
                if n1.val < n2.val:
                    cur_node.next = n1
                    n1 = n1.next
                else:
                    cur_node.next = n2
                    n2 = n2.next
                cur_node = cur_node.next

            rest_lists = n1 if n1 else n2
            cur_node.next = rest_lists
            return dummy_head.next

        list_node = lists[0]
        for i in range(1, len(lists)):
            list_node = merge_list(list_node, lists[i])

        return list_node


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
