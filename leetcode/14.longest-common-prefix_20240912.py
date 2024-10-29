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
        str_cmp = strs[0]
        for i in range(1, len(strs)):
            str_cmp = self.lcp(str_cmp, strs[i])
        return str_cmp

    def lcp(self, str1, str2):
        ans = ""
        n = min(len(str1), len(str2))
        for i in range(n):
            if str1[i] == str2[i]:
                ans += str1[i]
            else:
                break
        return ans


# @lc code=end


#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#
