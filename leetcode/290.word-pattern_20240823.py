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
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        n = len(pattern)
        hashmap_pattern2word = {}
        hashmap_word2pattern = {}
        for i in range(n):
            if (
                pattern[i] in hashmap_pattern2word
                and words[i] not in hashmap_word2pattern
            ):
                return False
            elif (
                pattern[i] not in hashmap_pattern2word
                and words[i] in hashmap_word2pattern
            ):
                return False
            elif (
                pattern[i] not in hashmap_pattern2word
                and words[i] not in hashmap_word2pattern
            ):
                hashmap_pattern2word[pattern[i]] = words[i]
                hashmap_word2pattern[words[i]] = pattern[i]
            elif (
                hashmap_pattern2word[pattern[i]] != words[i]
                or hashmap_word2pattern[words[i]] != pattern[i]
            ):
                return False
        return True


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
