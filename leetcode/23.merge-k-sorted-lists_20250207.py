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
        if not lists:
            return None

        def merge(list_1, list_2):
            dummy_head = ListNode()
            cur_node = dummy_head
            while list_1 and list_2:
                if list_1.val < list_2.val:
                    cur_node.next = list_1
                    list_1 = list_1.next
                else:
                    cur_node.next = list_2
                    list_2 = list_2.next
                cur_node = cur_node.next
            cur_node.next = list_1 or list_2
            return dummy_head.next
        
        result = lists[0]
        for i in range(1, len(lists)):
            result = merge(result, lists[i])
        
        return result
                

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

