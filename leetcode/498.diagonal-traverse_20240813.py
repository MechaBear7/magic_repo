#
# @lc app=leetcode.cn id=498 lang=python3
# @lcpr version=30204
#
# [498] 对角线遍历
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        num_row = len(mat)
        num_col = len(mat[0])
        temp_dict = {}
        for i in range(num_row):
            for j in range(num_col):
                if i + j in temp_dict:
                    temp_dict[i+j].append(mat[i][j])
                else:
                    temp_dict[i+j] = [mat[i][j]]
        res = []
        for s in range(num_row + num_col - 1):
            if s % 2 != 0:
                res.extend(temp_dict[s])
            else:
                res.extend(reversed(temp_dict[s]))
        return res
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,4]]\n
# @lcpr case=end

#

