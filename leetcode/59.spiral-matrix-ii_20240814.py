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
        ans = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        left, right, top, bottom = 0, n - 1, 0, n - 1
        while left <= right and top <= bottom:
            for col_idx in range(left, right+1):
                ans[top][col_idx] = num
                num += 1
            for row_idx in range(top+1, bottom+1):
                ans[row_idx][right] = num
                num += 1
            if left < right and top < bottom:
                for col_idx in range(right-1, left-1, -1):
                    ans[bottom][col_idx] = num
                    num += 1
                for row_idx in range(bottom-1, top, -1):
                    ans[row_idx][left] = num
                    num += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return ans
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

