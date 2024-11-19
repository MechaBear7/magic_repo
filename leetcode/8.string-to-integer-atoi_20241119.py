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
        idx = 0
        negative = False
        while idx < len(s) and s[idx] == " ":
            idx += 1
        if idx < len(s) and s[idx] == "-":
            negative = True
            idx += 1
        elif idx < len(s) and s[idx] == "+":
            idx += 1
        result = 0
        while idx < len(s):
            if not ord("0") <= ord(s[idx]) <= ord("9"):
                break
            result = 10 * result + int(s[idx])
            idx += 1
        if negative:
            result = -result
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result


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
