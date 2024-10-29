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
        if len(needle) > len(haystack):
            return -1
        match_idx = 0
        search_idx = 0
        while search_idx < len(haystack):
            # 找到匹配的首字母位置
            while search_idx < len(haystack) and haystack[search_idx] != needle[0]:
                search_idx += 1
            # 从该位置进行前向搜索
            forward_idx = search_idx
            while forward_idx < len(haystack) and match_idx < len(needle):
                if haystack[forward_idx] == needle[match_idx]:
                    match_idx += 1
                    forward_idx += 1
                else:
                    match_idx = 0
                    break
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
