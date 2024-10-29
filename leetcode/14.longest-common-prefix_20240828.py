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
        prefix = strs[0]
        n = len(strs)
        for i in range(1, n):
            prefix = self.lcp(prefix, strs[i])
        return prefix

    def lcp(self, s1, s2):
        prefix = ""
        n = min(len(s1), len(s2))
        for i in range(n):
            if s1[i] != s2[i]:
                break
            else:
                prefix += s1[i]
        return prefix


# @lc code=end


#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#
