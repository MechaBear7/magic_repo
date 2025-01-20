"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-20 16:33:16
LastEditors: Helei.Yang
LastEditTime: 2025-01-20 16:44:54
FilePath: /magic_repo/leetcode/221.maximal-square_20250120.py
Description: 
"""

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
        dp = [[1 if matrix[i][j] == "1" else 0 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == 1:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        max_len = 0
        for i in range(m):
            for j in range(n):
                max_len = max(max_len, dp[i][j])
        return max_len * max_len

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

