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
        if not strs:
            return ""
        str_cmp = strs[0]
        for i in range(1, len(strs)):
            str_cmp = self.lcp(str_cmp, strs[i])
            if not str_cmp:
                break
        return str_cmp

    def lcp(self, str1, str2):
        # 返回 str1 和 str2 的最长公共前缀
        index = 0
        max_length = min(len(str1), len(str2))
        while index < max_length and str1[index] == str2[index]:
            index += 1

        return str1[:index]


# @lc code=end


#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#
