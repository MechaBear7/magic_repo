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
        myset = set()
        max_len = 0
        left, right = 0, 0
        while right < len(s):
            while s[right] in myset:
                myset.remove(s[left])
                left += 1
            myset.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1
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
