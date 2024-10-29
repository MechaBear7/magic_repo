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
        hashmap_p2w = {}
        hashmap_w2p = {}
        n = len(words)
        for i in range(n):
            if pattern[i] not in hashmap_p2w and words[i] not in hashmap_w2p:
                hashmap_p2w[pattern[i]] = words[i]
                hashmap_w2p[words[i]] = pattern[i]
            elif (
                pattern[i] in hashmap_p2w
                and words[i] not in hashmap_w2p
                or pattern[i] not in hashmap_p2w
                and words[i] in hashmap_w2p
            ):
                return False
            elif (
                hashmap_p2w[pattern[i]] != words[i]
                or hashmap_w2p[words[i]] != pattern[i]
            ):
                return False
        return True

    def get_words(self, s):
        words = []
        left = 0
        while left < len(s):
            while left < len(s) and s[left] == " ":
                left += 1
            right = left
            while right < len(s) and s[right] != " ":
                right += 1
            if left < len(s):
                words.append(s[left:right])
            left = right
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
