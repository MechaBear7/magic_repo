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
        words = list(reversed(words))
        ans = words[0]
        n_words = len(words)
        for i in range(1, n_words):
            ans += " " + words[i]
        return ans

    def get_words(self, s):
        words = []
        left_idx = 0
        while left_idx < len(s):
            # 将 left_idx 从左至右移至非空格位
            while left_idx < len(s) and s[left_idx] == " ":
                left_idx += 1
            if left_idx == len(s):
                break
            # right_idx 从 left_idx 向右搜索到第一个空格位置
            right_idx = left_idx
            while right_idx < len(s) and s[right_idx] != " ":
                right_idx += 1
            words.append(s[left_idx:right_idx])
            left_idx = right_idx
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
