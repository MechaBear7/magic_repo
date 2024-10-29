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
        flag = 0
        a, b = list(a), list(b)
        for i in reversed(range(len(a))):
            count = flag + int(a[i]) + int(b[i])
            if count == 3:
                flag = 1
                a[i] = "1"
            elif count == 2:
                flag = 1
                a[i] = "0"
            elif count == 1:
                flag = 0
                a[i] = "1"
            else:
                flag = 0
                a[i] = "0"
        if flag == 1:
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
