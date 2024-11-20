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
        stk = []
        for d in s:
            if d != "]":
                stk.append(d)
            else:
                word = []
                while stk and stk[-1] != "[":
                    word.append(stk.pop())
                word = list(reversed(word))
                stk.pop()
                cnt = []
                while stk and ord("0") <= ord(stk[-1]) <= ord("9"):
                    cnt.append(stk.pop())
                cnt = int("".join(reversed(cnt)))
                stk.extend(word * cnt)
        return "".join(stk)


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
