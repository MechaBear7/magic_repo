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
        # store[i] 表示引用 i 次论文的个数
        store = [0 for _ in range(n + 1)]
        for cite in citations:
            if cite > n:
                store[n] += 1
            else:
                store[cite] += 1
        cites = 0
        i = n
        while i >= 0:
            cites += store[i]
            if cites >= i:
                return i
            i -= 1


# @lc code=end


#
# @lcpr case=start
# [3,0,6,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,1]\n
# @lcpr case=end

#
