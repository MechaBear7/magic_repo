#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30204
#
# [54] 螺旋矩阵
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        # m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and top <= bottom:
            for col_idx in range(left, right + 1):
                result.append(matrix[top][col_idx])
            for row_idx in range(top + 1, bottom + 1):
                result.append(matrix[row_idx][right])
            if left < right and top < bottom:
                for col_idx in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom][col_idx])
                for row_idx in range(bottom - 1, top, -1):
                    result.append(matrix[row_idx][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return result


# @lc code=end


#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#
