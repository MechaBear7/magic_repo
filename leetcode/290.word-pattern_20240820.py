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
        map_pattern2word = {}
        map_word2pattern = {}
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            if words[i] not in map_word2pattern and pattern[i] in map_pattern2word:
                return False
            elif words[i] in map_word2pattern and pattern[i] not in map_pattern2word:
                return False
            elif (
                words[i] not in map_word2pattern and pattern[i] not in map_pattern2word
            ):
                map_word2pattern[words[i]] = pattern[i]
                map_pattern2word[pattern[i]] = words[i]
            else:
                if (
                    map_word2pattern[words[i]] != pattern[i]
                    or map_pattern2word[pattern[i]] != words[i]
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
