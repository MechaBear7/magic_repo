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
        my_dict = {}
        num_cols = len(mat)
        num_rows = len(mat[0])
        for i in range(num_cols):
            for j in range(num_rows):
                if i+j in my_dict:
                    my_dict[i+j].append(mat[i][j])
                else:
                    my_dict[i+j] = [mat[i][j]]
        res = []
        for i in range(num_cols + num_rows - 1):
            if i % 2 != 0:
                res.extend(my_dict[i])
            else:
                res.extend(reversed(my_dict[i]))
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

