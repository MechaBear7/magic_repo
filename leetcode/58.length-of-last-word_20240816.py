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
        words = s.split(" ")
        for word in reversed(words):
            if len(word) != 0:
                return len(word)
        return 0


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
