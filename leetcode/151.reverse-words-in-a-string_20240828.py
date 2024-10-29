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
        print(words)
        ans = " ".join(reversed(words))
        return ans

    def get_words(self, s):
        words = []
        left_index = 0
        while left_index < len(s):
            # 将 left_index 移动到第一个字母位，或最后一个字符的后一位
            while left_index < len(s) and s[left_index] == " ":
                left_index += 1
            # 将 right_index 移动到第一个空格位，或最后一个字符的后一位
            right_index = left_index
            while right_index < len(s) and s[right_index] != " ":
                right_index += 1
            if left_index < len(s):
                words.append(s[left_index:right_index])
            left_index = right_index
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
