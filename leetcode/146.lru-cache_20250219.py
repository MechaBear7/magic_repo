#
# @lc app=leetcode.cn id=146 lang=python3
# @lcpr version=30204
#
# [146] LRU 缓存
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class DListNode:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.head = DListNode()
        self.tail = DListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.removeNode(node)
        self.addNode(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.removeNode(node)
            node.value = value
            self.addNode(node)
        else:
            node = DListNode(key, value)
            self.hashmap[key] = node
            self.addNode(node)
            self.size += 1
            if self.size > self.capacity:
                node = self.tail.prev
                self.removeNode(node)
                self.hashmap.pop(node.key)
                self.size -= 1

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        return node
    
    def addNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        node.prev.next = node
        node.next.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end



