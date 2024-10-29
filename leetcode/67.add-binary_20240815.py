#
# @lc app=leetcode.cn id=67 lang=python3
# @lcpr version=30204
#
# [67] 二进制求和
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        while len(a) > len(b):
            b = "0" + b
        while len(a) < len(b):
            a = "0" + a
        tmp = 0
        a, b = list(a), list(b)
        for i in reversed(range(len(a))):
            cur = int(a[i]) + int(b[i]) + tmp
            if cur == 3:
                a[i] = "1"
                tmp = 1
            elif cur == 2:
                a[i] = "0"
                tmp = 1
            elif cur == 1:
                a[i] = "1"
                tmp = 0
            else:
                a[i] = "0"
                tmp = 0
        if tmp == 1:
            a = ["1"] + a
        return "".join(a)


# @lc code=end


#
# @lcpr case=start
# "11"\n"1"\n
# @lcpr case=end

# @lcpr case=start
# "1010"\n"1011"\n
# @lcpr case=end

#
