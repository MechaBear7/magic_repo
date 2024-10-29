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
        result = ""
        flag = 0
        i = len(a) - 1
        while i >= 0:
            count = int(a[i]) + int(b[i]) + flag
            if count == 3:
                flag = 1
                result = "1" + result
            elif count == 2:
                flag = 1
                result = "0" + result
            elif count == 1:
                flag = 0
                result = "1" + result
            else:
                flag = 0
                result = "0" + result
            i -= 1
        if flag == 1:
            result = "1" + result
        return result


# @lc code=end


#
# @lcpr case=start
# "11"\n"1"\n
# @lcpr case=end

# @lcpr case=start
# "1010"\n"1011"\n
# @lcpr case=end

#
