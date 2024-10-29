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

        search_idx = 0
        while search_idx < len(haystack):
            # 将 search_idx 移至首字母匹配位置
            while search_idx < len(haystack) and haystack[search_idx] != needle[0]:
                search_idx += 1
            # 向后检索检查是否匹配
            match_idx = 0
            while search_idx + match_idx < len(haystack) and match_idx < len(needle):
                if haystack[search_idx + match_idx] != needle[match_idx]:
                    break
                match_idx += 1
            if match_idx == len(needle):
                return search_idx
            search_idx += 1

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
