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
        hashmap_st = {}
        hashmap_ts = {}
        for i in range(len(s)):
            if t[i] in hashmap_ts and s[i] not in hashmap_st:
                return False
            elif t[i] not in hashmap_ts and s[i] in hashmap_st:
                return False
            elif t[i] not in hashmap_ts and s[i] not in hashmap_st:
                hashmap_ts[t[i]] = s[i]
                hashmap_st[s[i]] = t[i]
            elif hashmap_ts[t[i]] != s[i] or hashmap_st[s[i]] != t[i]:
                return False
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
