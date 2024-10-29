#
# @lc app=leetcode.cn id=28 lang=python3
# @lcpr version=30204
#
# [28] 找出字符串中第一个匹配项的下标
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        for serach_idx in range(len(haystack)):
            if haystack[serach_idx] != needle[0]:
                continue
            match = True
            for match_idx in range(len(needle)):
                if (
                    serach_idx + match_idx >= len(haystack)
                    or haystack[serach_idx + match_idx] != needle[match_idx]
                ):
                    match = False
                    break
                else:
                    continue
            if match:
                return serach_idx
        return -1


# @lc code=end


#
# @lcpr case=start
# "sadbutsad"\n"sad"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n"leeto"\n
# @lcpr case=end

#
