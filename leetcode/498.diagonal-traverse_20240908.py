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
        hashmap = {}
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if i + j not in hashmap:
                    hashmap[i + j] = [mat[i][j]]
                else:
                    hashmap[i + j].append(mat[i][j])

        result = []
        for i in range(m + n - 1):
            if i % 2 == 0:
                result.extend(reversed(hashmap[i]))
            else:
                result.extend(hashmap[i])
        return result


# @lc code=end


#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,4]]\n
# @lcpr case=end

#
