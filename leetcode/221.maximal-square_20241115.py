#
# @lc app=leetcode.cn id=221 lang=python3
# @lcpr version=30204
#
# [221] 最大正方形
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # dp[i][j] 表示以 i,j 为右下角坐标的最大正方形边长
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            dp[row][0] = int(matrix[row][0])
        for col in range(n):
            dp[0][col] = int(matrix[0][col])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
                    if dp[i - 1][j - 1] >= dp[i][j]:
                        dp[i][j] += 1
        max_ans = 0
        for i in range(m):
            for j in range(n):
                max_ans = max(max_ans, dp[i][j] * dp[i][j])

        return max_ans


# @lc code=end


#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0","1"],["1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

#
