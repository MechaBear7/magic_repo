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
        map_st, map_ts = {}, {}
        for i in range(len(s)):
            if s[i] not in map_st and t[i] not in map_ts:
                map_st[s[i]] = t[i]
                map_ts[t[i]] = s[i]
            elif (s[i] in map_st and t[i] not in map_ts) or (
                s[i] not in map_st and t[i] in map_ts
            ):
                return False
            elif map_st[s[i]] != t[i] or map_ts[t[i]] != s[i]:
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
