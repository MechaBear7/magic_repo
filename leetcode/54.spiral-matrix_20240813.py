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
        if not matrix or not matrix[0]:
            return list()
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        res = []
        while left <= right and top <= bottom:
            for col in range(left, right+1):
                res.append(matrix[top][col])
            for row in range(top+1, bottom+1):
                res.append(matrix[row][right])
            if left < right and top < bottom:
                for col in range(right-1, left-1, -1):
                    res.append(matrix[bottom][col])
                for row in range(bottom-1, top, -1):
                    res.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res

# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

