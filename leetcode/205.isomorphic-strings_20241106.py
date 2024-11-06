#
# @lc app=leetcode.cn id=205 lang=python3
# @lcpr version=30204
#
# [205] 同构字符串
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        s2t, t2s = {}, {}
        for i in range(n):
            if (s[i] in s2t and t[i] not in t2s) or (s[i] not in s2t and t[i] in t2s):
                return False
            elif s[i] not in s2t and t[i] not in t2s:
                s2t[s[i]] = t[i]
                t2s[t[i]] = s[i]
            elif s2t[s[i]] != t[i] or t2s[t[i]] != s[i]:
                return False
            else:
                continue
        return True


# @lc code=end


#
# @lcpr case=start
# "egg"\n"add"\n
# @lcpr case=end

# @lcpr case=start
# "foo"\n"bar"\n
# @lcpr case=end

# @lcpr case=start
# "paper"\n"title"\n
# @lcpr case=end

#
