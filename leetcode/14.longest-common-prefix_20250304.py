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
        def find_prefix(str1, str2):
            end = min(len(str1), len(str2))
            for idx in range(end):
                if str1[idx] != str2[idx]:
                    return str1[:idx]
            return str1[:end]

        result = strs[0]
        for idx in range(1, len(strs)):
            result = find_prefix(result, strs[idx])
        return result

# @lc code=end



#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#

