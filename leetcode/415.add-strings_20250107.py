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
        flag = 0
        result = []
        for i in reversed(range(len(num1))):
            count = flag + int(num1[i]) + int(num2[i])
            result.append(str(count % 10))
            flag = count // 10
        if flag == 1:
            result.append("1")
        return "".join(reversed(result))
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

