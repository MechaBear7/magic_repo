#
# @lc app=leetcode.cn id=415 lang=python3
# @lcpr version=30204
#
# [415] 字符串相加
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        while len(num1) < len(num2):
            num1 = "0" + num1
        while len(num1) > len(num2):
            num2 = "0" + num2
        result = ""
        flag = 0
        n = len(num1)
        for i in range(n - 1, -1, -1):
            cnt = flag + int(num1[i]) + int(num2[i])
            flag = 1 if cnt > 9 else 0
            result = str(cnt % 10) + result
        if flag == 1:
            result = "1" + result
        return result


# @lc code=end


#
# @lcpr case=start
# "11"\n"123"\n
# @lcpr case=end

# @lcpr case=start
# "456"\n"77"\n
# @lcpr case=end

# @lcpr case=start
# "0"\n"0"\n
# @lcpr case=end

#
