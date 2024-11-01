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
        left2right = [1 for _ in range(n)]
        right2left = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1
        for i in reversed(range(0, n - 1)):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1

        answer = 0
        for i in range(n):
            answer += max(left2right[i], right2left[i])

        return answer


# @lc code=end


#
# @lcpr case=start
# [1,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

#
