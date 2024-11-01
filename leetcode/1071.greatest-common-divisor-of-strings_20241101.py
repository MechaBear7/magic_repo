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
        min_len = min(len(str1), len(str2))
        for i in reversed(range(min_len)):
            if len(str1) % (i + 1) == 0 and len(str2) % (i + 1) == 0:
                piece_str = str1[: i + 1]
                if str1 == (len(str1) // (i + 1)) * piece_str and str2 == (len(str2) // (i + 1)) * piece_str:
                    return piece_str
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
