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
        citations_store = [0 for _ in range(len(citations) + 1)]  # citations_store[i] 代表引用次数为 i 的论文数量
        for cite_num in citations:
            if cite_num > len(citations):
                citations_store[len(citations)] += 1
            else:
                citations_store[cite_num] += 1

        citation_counts = 0
        for i in reversed(range(len(citations_store))):
            citation_counts += citations_store[i]
            if citation_counts >= i:
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
