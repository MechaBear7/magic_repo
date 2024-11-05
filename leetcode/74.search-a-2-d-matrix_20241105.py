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
        m, n = len(matrix), len(matrix[0])

        def get_location(num):
            row_idx = num // n
            col_idx = num % n
            return row_idx, col_idx

        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            row_idx, col_idx = get_location(mid)
            if matrix[row_idx][col_idx] == target:
                return True
            elif matrix[row_idx][col_idx] < target:
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
