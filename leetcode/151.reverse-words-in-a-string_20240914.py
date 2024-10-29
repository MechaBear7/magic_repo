#
# @lc app=leetcode.cn id=151 lang=python3
# @lcpr version=30204
#
# [151] 反转字符串中的单词
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = self.getWords(s)
        print(words)
        return " ".join(reversed(words))

    def getWords(self, s):
        words = []
        left, right = 0, 0
        while left < len(s):
            while left < len(s) and s[left] == " ":
                left += 1
            right = left + 1
            while right < len(s) and s[right] != " ":
                right += 1
            if left < len(s):
                words.append(s[left:right])
            left = right + 1
        return words


# @lc code=end


#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

#
