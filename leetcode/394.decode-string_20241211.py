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
        for d in s:
            if d != "]":
                result.append(d)
            else:
                word = []
                while result[-1] != "[":
                    word.append(result.pop())
                result.pop()
                word = list(reversed(word))
                num = []
                while result and ord("0") <= ord(result[-1]) <= ord("9"):
                    num.append(result.pop())
                num = int("".join(list(reversed(num))))
                result.extend(word * num)
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
