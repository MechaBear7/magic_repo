#
# @lc app=leetcode.cn id=74 lang=python3
# @lcpr version=30204
#
# [74] 搜索二维矩阵
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_location(num_col, n):
            new_row = n // num_col
            new_col = n % num_col
            return new_row, new_col

        num_row = len(matrix)
        num_col = len(matrix[0])
        left = 0
        right = num_row * num_col - 1
        while left <= right:
            mid = left + (right - left) // 2
            row, col = get_location(num_col, mid)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


# @lc code=end


#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#
