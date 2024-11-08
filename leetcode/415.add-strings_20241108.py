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
        while len(num2) < len(num1):
            num2 = "0" + num2

        n = len(num1) - 1
        ans = ""
        flag = 0
        while n >= 0:
            count = flag + int(num1[n]) + int(num2[n])
            flag = 1 if count > 9 else 0
            ans = str(count % 10) + ans
            n -= 1
        if flag == 1:
            ans = "1" + ans
        return ans


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
