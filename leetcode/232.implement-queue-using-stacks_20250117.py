"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-17 13:36:59
LastEditors: Helei.Yang
LastEditTime: 2025-01-17 13:41:06
FilePath: /magic_repo/leetcode/232.implement-queue-using-stacks_20250117.py
Description: 
"""

#
# @lc app=leetcode.cn id=232 lang=python3
# @lcpr version=30204
#
# [232] 用栈实现队列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class MyQueue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        self.move()
        return self.stk2.pop()

    def peek(self) -> int:
        self.move()
        return self.stk2[-1]

    def empty(self) -> bool:
        return len(self.stk1) == 0 and len(self.stk2) == 0

    def move(self):
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end



#
# @lcpr case=start
# ["MyQueue", "push", "push", "peek", "pop", "empty"][[], [1], [2], [], [], []]\n
# @lcpr case=end

#

