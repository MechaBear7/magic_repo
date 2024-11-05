#
# @lc app=leetcode.cn id=707 lang=python3
# @lcpr version=30204
#
# [707] 设计链表
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.dummy_head = Node()

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        else:
            cur_node = self.dummy_head
            for _ in range(index):
                cur_node = cur_node.next
            return cur_node.next.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.dummy_head.next
        self.dummy_head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        cur_node = self.dummy_head
        for _ in range(self.size):
            cur_node = cur_node.next
        cur_node.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            cur_node = self.dummy_head
            for _ in range(index):
                cur_node = cur_node.next
            new_node.next = cur_node.next
            cur_node.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        cur_node = self.dummy_head
        for _ in range(index):
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
