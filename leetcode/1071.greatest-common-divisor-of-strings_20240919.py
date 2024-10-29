#
# @lc app=leetcode.cn id=1071 lang=python3
# @lcpr version=30204
#
# [1071] 字符串的最大公因子
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        for i in reversed(range(1, min(len1, len2) + 1)):
            if len1 % i == 0 and len2 % i == 0:
                c1, c2 = len1 // i, len2 // i
                if c1 * str1[:i] == str1 and c2 * str1[:i] == str2:
                    return str1[:i]
        return ""


# @lc code=end


#
# @lcpr case=start
# "ABCABC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "ABABAB"\n"ABAB"\n
# @lcpr case=end

# @lcpr case=start
# "LEET"\n"CODE"\n
# @lcpr case=end

#
