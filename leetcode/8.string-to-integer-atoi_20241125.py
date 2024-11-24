#
# @lc app=leetcode.cn id=8 lang=python3
# @lcpr version=30204
#
# [8] 字符串转换整数 (atoi)
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -(1 << 31), (1 << 31) - 1
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i == len(s):
            return 0
        # 检查符号位
        negative = False
        if s[i] in ("+", "-"):
            negative = s[i] == "-"
            i += 1
        result = []
        while i < len(s) and ord("0") <= ord(s[i]) <= ord("9"):
            result.append(s[i])
            i += 1
        if len(result) == 0:
            return 0
        else:
            num = int("".join(result))
            if negative:
                num = -num
            if num < INT_MIN:
                return INT_MIN
            elif num > INT_MAX:
                return INT_MAX
            else:
                return num


# @lc code=end


#
# @lcpr case=start
# "42"\n
# @lcpr case=end

# @lcpr case=start
# " -042"\n
# @lcpr case=end

# @lcpr case=start
# "1337c0d3"\n
# @lcpr case=end

# @lcpr case=start
# "0-1"\n
# @lcpr case=end

# @lcpr case=start
# "words and 987"\n
# @lcpr case=end

#
