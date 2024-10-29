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
        words = self.get_words(s)
        return " ".join(reversed(words))

    def get_words(self, s):
        words = []
        left_idx = 0
        right_idx = 0
        while left_idx < len(s):
            # left_idx 移动到第一个字母位
            while left_idx < len(s) and s[left_idx] == " ":
                left_idx += 1
            right_idx = left_idx
            while right_idx < len(s) and s[right_idx] != " ":
                right_idx += 1
            if left_idx < len(s):
                words.append(s[left_idx:right_idx])
            left_idx = right_idx + 1

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
