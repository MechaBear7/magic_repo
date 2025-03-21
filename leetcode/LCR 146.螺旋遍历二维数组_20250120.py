#
# @lc app=leetcode.cn id=LCR 146 lang=python3
# @lcpr version=30204
#
# [LCR 146] 螺旋遍历二维数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        result = []
        if len(array) == 0:
            return result
        top, bottom, left, right = 0, len(array) - 1, 0, len(array[0]) - 1
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result.append(array[top][col])
            for row in range(top + 1, bottom + 1):
                result.append(array[row][right])
            if top < bottom and left < right:
                for col in reversed(range(left, right)):
                    result.append(array[bottom][col])
                for row in reversed(range(top + 1, bottom)):
                    result.append(array[row][left])
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        return result

# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[8,9,4],[7,6,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]\n
# @lcpr case=end

#

