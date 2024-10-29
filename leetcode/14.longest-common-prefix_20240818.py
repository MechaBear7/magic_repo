#
# @lc app=leetcode.cn id=14 lang=python3
# @lcpr version=30204
#
# [14] 最长公共前缀
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or len(strs[0]) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = self.cmp_string(prefix, strs[i])
            if len(prefix) == 0:
                break
        return prefix

    def cmp_string(self, str1, str2):
        length = 0
        max_length = min(len(str1), len(str2))
        for i in range(max_length):
            if str1[i] != str2[i]:
                break
            else:
                length += 1
        return str1[:length]


# @lc code=end


#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#
