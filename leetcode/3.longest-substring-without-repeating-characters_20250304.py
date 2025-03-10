#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        hashmap = {}
        left, right = 0, 0
        while right < len(s):
            while s[right] in hashmap:
                hashmap.pop(s[left])
                left += 1

            hashmap[s[right]] = right
            right += 1
            max_len = max(max_len, right - left)
        return max_len
                

# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

