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
        my_set = set()
        left_idx, right_idx = 0, 0
        max_length = 0
        while right_idx < len(s):
            while s[right_idx] in my_set:
                my_set.remove(s[left_idx])
                left_idx += 1
            my_set.add(s[right_idx])
            right_idx += 1
            max_length = max(max_length, right_idx - left_idx)
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
