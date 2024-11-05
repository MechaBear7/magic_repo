#
# @lc app=leetcode.cn id=392 lang=python3
# @lcpr version=30204
#
# [392] 判断子序列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        s_idx, t_idx = 0, 0
        while s_idx < len(s) and t_idx < len(t):
            while t_idx < len(t) and t[t_idx] != s[s_idx]:
                t_idx += 1
            if t_idx == len(t):
                return False
            else:
                s_idx, t_idx = s_idx + 1, t_idx + 1
        return s_idx == len(s)


# @lc code=end


#
# @lcpr case=start
# "abc"\n"ahbgdc"\n
# @lcpr case=end

# @lcpr case=start
# "axc"\n"ahbgdc"\n
# @lcpr case=end

#
