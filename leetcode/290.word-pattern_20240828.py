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
        words = s.strip().split(" ")
        if len(words) != len(pattern):
            return False
        n = len(words)
        map_pattern2word = {}
        map_word2pattern = {}
        for i in range(n):
            if pattern[i] not in map_pattern2word and words[i] not in map_word2pattern:
                map_pattern2word[pattern[i]] = words[i]
                map_word2pattern[words[i]] = pattern[i]
            elif (
                pattern[i] in map_pattern2word and words[i] not in map_word2pattern
            ) or (pattern[i] not in map_pattern2word and words[i] in map_word2pattern):
                return False
            elif (
                map_pattern2word[pattern[i]] != words[i]
                or map_word2pattern[words[i]] != pattern[i]
            ):
                return False
            else:
                continue
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
