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
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        # 建立伪头结点和尾节点
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
        self.remove_node(node)
        self.add_node_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            new_node = DListNode(key, value)
            self.hashmap[key] = new_node
            self.add_node_to_head(new_node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.remove_node(self.tail.prev)
                self.hashmap.pop(removed.key)
                self.size -= 1
        else:
            node = self.hashmap[key]
            node.value = value
            self.remove_node(node)
            self.add_node_to_head(node)

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def add_node_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end



