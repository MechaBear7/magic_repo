#
# @lc app=leetcode.cn id=58 lang=python3
# @lcpr version=30204
#
# [58] 最后一个单词的长度
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right_idx = len(s) - 1
        while right_idx >= 0 and s[right_idx] == " ":
            right_idx -= 1
        left_idx = right_idx
        while left_idx >= 0 and s[left_idx] != " ":
            left_idx -= 1
        return right_idx - left_idx


# @lc code=end


#
# @lcpr case=start
# "Hello World"\n
# @lcpr case=end

# @lcpr case=start
# "   fly me   to   the moon  "\n
# @lcpr case=end

# @lcpr case=start
# "luffy is still joyboy"\n
# @lcpr case=end

#
