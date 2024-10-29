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
        while len(a) < len(b):
            a = "0" + a
        while len(a) > len(b):
            b = "0" + b
        list_a = list(a)
        list_b = list(b)
        tmp = 0
        for i in reversed(range(len(list_a))):
            count = int(list_a[i]) + int(list_b[i]) + tmp
            if count == 3:
                list_a[i] = "1"
                tmp = 1
            elif count == 2:
                list_a[i] = "0"
                tmp = 1
            elif count == 1:
                list_a[i] = "1"
                tmp = 0
            else:
                list_a[i] = "0"
                tmp = 0
        if tmp == 1:
            list_a = ["1"] + list_a
        return "".join(list_a)


# @lc code=end


#
# @lcpr case=start
# "11"\n"1"\n
# @lcpr case=end

# @lcpr case=start
# "1010"\n"1011"\n
# @lcpr case=end

#
