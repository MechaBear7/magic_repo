#
# @lc app=leetcode.cn id=240 lang=python3
# @lcpr version=30204
#
# [240] 搜索二维矩阵 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

# @lc code=end



#
# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n20\n
# @lcpr case=end

#

