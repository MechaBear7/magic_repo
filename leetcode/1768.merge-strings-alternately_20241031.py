#
# @lc app=leetcode.cn id=1768 lang=python3
# @lcpr version=30204
#
# [1768] 交替合并字符串
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        return result


# @lc code=end


#
# @lcpr case=start
# "abc"\n"pqr"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"pqrs"\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"pq"\n
# @lcpr case=end

#
