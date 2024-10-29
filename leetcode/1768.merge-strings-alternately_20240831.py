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
        p1, p2 = 0, 0
        flag = 0
        while p1 < len(word1) and flag == 0 or p2 < len(word2) and flag == 1:
            if flag == 0:
                result += word1[p1]
                p1 += 1
                flag = 1
            else:
                result += word2[p2]
                p2 += 1
                flag = 0
        if p1 != len(word1):
            result += word1[p1:]
        else:
            result += word2[p2:]
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
