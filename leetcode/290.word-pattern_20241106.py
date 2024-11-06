#
# @lc app=leetcode.cn id=290 lang=python3
# @lcpr version=30204
#
# [290] 单词规律
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = self.get_words(s)
        if len(pattern) != len(words):
            return False

        p2s, s2p = {}, {}
        n = len(words)
        for i in range(n):
            if pattern[i] in p2s and words[i] not in s2p or pattern[i] not in p2s and words[i] in s2p:
                return False
            elif pattern[i] not in p2s and words[i] not in s2p:
                p2s[pattern[i]] = words[i]
                s2p[words[i]] = pattern[i]
            elif p2s[pattern[i]] != words[i] or s2p[words[i]] != pattern[i]:
                return False
            else:
                continue
        return True

    def get_words(self, s):
        words = []
        left_idx = 0
        while left_idx < len(s):
            while left_idx < len(s) and s[left_idx] == " ":
                left_idx += 1
            right_idx = left_idx
            while right_idx < len(s) and s[right_idx] != " ":
                right_idx += 1
            if left_idx < right_idx:
                words.append(s[left_idx:right_idx])
            left_idx = right_idx + 1
        return words


# @lc code=end


#
# @lcpr case=start
# "abba"\n"dog cat cat dog"\n
# @lcpr case=end

# @lcpr case=start
# "abba"\n"dog cat cat fish"\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n"dog cat cat dog"\n
# @lcpr case=end

#
