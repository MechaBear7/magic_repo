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
        n = len(s)
        if n <= 1:
            return n
        my_set = set()
        window_left, window_right = 0, 0
        max_length = 0
        while window_right < len(s):
            while s[window_right] in my_set:
                my_set.remove(s[window_left])
                window_left += 1
            my_set.add(s[window_right])
            window_right += 1
            max_length = max(max_length, window_right - window_left)

        return max_length


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
