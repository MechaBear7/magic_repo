#
# @lc app=leetcode.cn id=59 lang=python3
# @lcpr version=30204
#
# [59] 螺旋矩阵 II
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        num = 1
        result = [[0 for _ in range(n)] for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                result[top][col] = num
                num += 1
            for row in range(top + 1, bottom + 1):
                result[row][right] = num
                num += 1
            if left < right and top < bottom:
                for col in range(right - 1, left - 1, -1):
                    result[bottom][col] = num
                    num += 1
                for row in range(bottom - 1, top, -1):
                    result[row][left] = num
                    num += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return result


# @lc code=end


#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
