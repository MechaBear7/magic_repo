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
        n = len(strs)
        cmp_str = strs[0]
        for i in range(1, n):
            cmp_str = self.lcp(cmp_str, strs[i])
        return cmp_str

    def lcp(self, str1: str, str2: str) -> str:
        length = 0
        max_length = min(len(str1), len(str2))
        while length < max_length:
            if str1[length] != str2[length]:
                break
            length += 1
        return str1[:length] if length != 0 else ""


# @lc code=end


#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#
