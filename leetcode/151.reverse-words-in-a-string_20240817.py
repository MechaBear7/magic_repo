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
        words = []
        left_idx = 0
        while left_idx < len(s):
            while left_idx < len(s) and s[left_idx] == " ":
                left_idx += 1  # 将 left_idx 移到第一个字母位置
            if left_idx == len(s):
                break
            else:
                for right_idx in range(left_idx, len(s) + 1):
                    if right_idx == len(s) or s[right_idx] == " ":
                        words.append(s[left_idx:right_idx])
                        break
                left_idx = right_idx
        ans = ""
        for word in reversed(words):
            ans = ans + " " + word
        ans = ans[1:]
        return ans


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
