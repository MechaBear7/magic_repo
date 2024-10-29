#
# @lc app=leetcode.cn id=73 lang=python3
# @lcpr version=30204
#
# [73] 矩阵置零
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        col_set = set()
        num_row = len(matrix)
        num_col = len(matrix[0])
        for i in range(num_row):
            for j in range(num_col):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        for row_idx in row_set:
            for col_idx in range(num_col):
                matrix[row_idx][col_idx] = 0

        for row_idx in range(num_row):
            for col_idx in col_set:
                matrix[row_idx][col_idx] = 0


# @lc code=end


#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#
