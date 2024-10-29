#
# @lc app=leetcode.cn id=135 lang=python3
# @lcpr version=30204
#
# [135] 分发糖果
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l2r = [1 for _ in range(n)]
        r2l = [1 for _ in range(n)]
        for i in range(n):
            if i != 0 and ratings[i] > ratings[i - 1]:
                l2r[i] = l2r[i - 1] + 1
        for i in reversed(range(n)):
            if i != n - 1 and ratings[i] > ratings[i + 1]:
                r2l[i] = r2l[i + 1] + 1
        result = 0
        for i in range(n):
            result += max(l2r[i], r2l[i])
        return result


# @lc code=end


#
# @lcpr case=start
# [1,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

#
