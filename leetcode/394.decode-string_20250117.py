"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-17 13:48:37
LastEditors: Helei.Yang
LastEditTime: 2025-01-17 13:56:22
FilePath: /magic_repo/leetcode/394.decode-string_20250117.py
Description: 
"""

#
# @lc app=leetcode.cn id=394 lang=python3
# @lcpr version=30204
#
# [394] 字符串解码
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            if s[i] != "]":
                result.append(s[i])
            else:
                word = []
                while len(result) != 0 and result[-1] != "[":
                    word.append(result.pop())
                result.pop()
                num = []
                while len(result) != 0 and ord("0") <= ord(result[-1]) <= ord("9"):
                    num.append(result.pop())
                new_word = int("".join(reversed(num))) * list(reversed(word))
                result.extend(new_word)
        return "".join(result)

# @lc code=end



#
# @lcpr case=start
# "3[a]2[bc]"\n
# @lcpr case=end

# @lcpr case=start
# "3[a2[c]]"\n
# @lcpr case=end

# @lcpr case=start
# "2[abc]3[cd]ef"\n
# @lcpr case=end

# @lcpr case=start
# "abc3[cd]xyz"\n
# @lcpr case=end

#

