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
        cmp_str = strs[0]

        for i in range(1, len(strs)):
            cmp_str = self.lcp(cmp_str, strs[i])

        return cmp_str

    def lcp(self, str1, str2):
        max_len = min(len(str1), len(str2))

        idx = 0
        while idx < max_len:
            if str1[idx] != str2[idx]:
                break
            idx += 1

        return str1[:idx]


# @lc code=end


#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#
