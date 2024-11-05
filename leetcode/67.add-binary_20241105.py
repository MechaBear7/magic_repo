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
        result = ["" for _ in range(len(a))]
        i = len(a) - 1
        while i >= 0:
            num = flag + int(a[i]) + int(b[i])
            if num == 3:
                result[i] = "1"
                flag = 1
            elif num == 2:
                result[i] = "0"
                flag = 1
            elif num == 1:
                result[i] = "1"
                flag = 0
            else:
                result[i] = "0"
                flag = 0
            i -= 1
        if flag == 1:
            result = ["1"] + result
        return "".join(result)


# @lc code=end


#
# @lcpr case=start
# "11"\n"1"\n
# @lcpr case=end

# @lcpr case=start
# "1010"\n"1011"\n
# @lcpr case=end

#
