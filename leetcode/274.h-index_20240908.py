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
        # 定义 store 代表 引用次数为 i 的论文的篇数
        store = [0 for i in range(n + 1)]
        for cite in citations:
            if cite > n:
                store[n] += 1
            else:
                store[cite] += 1
        cites = 0
        for i in reversed(range(n + 1)):
            cites += store[i]
            if cites >= i:
                return i
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
