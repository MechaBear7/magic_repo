#
# @lc app=leetcode.cn id=274 lang=python3
# @lcpr version=30204
#
# [274] H 指数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        store = [0 for _ in range(n + 1)]
        for i in range(n):
            if citations[i] > n:
                store[n] += 1
            else:
                store[citations[i]] += 1
        cites = 0
        for i in reversed(range(n + 1)):
            cites += store[i]
            if cites >= n:
                return n
            n -= 1
        return 0


# @lc code=end


#
# @lcpr case=start
# [3,0,6,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,1]\n
# @lcpr case=end

#
