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
        result_1 = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                result_1[i] = result_1[i - 1] + 1
        result_2 = [1 for _ in range(n)]
        for i in reversed(range(n - 1)):
            if ratings[i] > ratings[i + 1]:
                result_2[i] = result_2[i + 1] + 1
        result = 0
        for i in range(n):
            result += max(result_1[i], result_2[i])
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
