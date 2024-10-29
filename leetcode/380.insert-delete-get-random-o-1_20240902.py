#
# @lc app=leetcode.cn id=380 lang=python3
# @lcpr version=30204
#
# [380] O(1) 时间插入、删除和获取随机元素
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class RandomizedSet:
    def __init__(self):
        self.hashmap = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.data.append(val)
            self.hashmap[val] = len(self.data) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            val_idx = self.hashmap[val]
            self.hashmap[self.data[-1]] = val_idx
            self.data[val_idx], self.data[-1] = self.data[-1], self.data[val_idx]
            del self.hashmap[val]
            del self.data[-1]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
