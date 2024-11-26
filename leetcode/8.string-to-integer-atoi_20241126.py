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
        idx = 0
        while idx < len(s) and s[idx] == " ":
            idx += 1
        if idx == len(s):
            return 0
        # 检查下一位是否是符号位
        negative = False
        if s[idx] in ("+", "-"):
            negative = s[idx] == "-"
            idx += 1
        ans = 0
        while idx < len(s) and ord("0") <= ord(s[idx]) <= ord("9"):
            ans = ans * 10 + int(s[idx])
            idx += 1
        if negative:
            ans = -ans
        INT_MIN, INT_MAX = -(1 << 31), (1 << 31) - 1
        if ans < INT_MIN:
            return INT_MIN
        elif ans > INT_MAX:
            return INT_MAX
        else:
            return ans


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
