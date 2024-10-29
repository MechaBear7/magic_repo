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
        my_dict = {}
        for i in range(num_row):
            for j in range(num_col):
                if i + j not in my_dict:
                    my_dict[i + j] = [mat[i][j]]
                else:
                    my_dict[i + j].append(mat[i][j])
        ans = []
        for i in range(len(my_dict)):
            if i % 2 != 0:
                ans.extend(my_dict[i])
            else:
                ans.extend(reversed(my_dict[i]))
        return ans


# @lc code=end


#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,4]]\n
# @lcpr case=end

#
