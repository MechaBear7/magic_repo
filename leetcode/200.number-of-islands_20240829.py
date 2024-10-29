#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30204
#
# [200] 岛屿数量
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}
        for direction in directions:
            row_idx = direction[0] + i
            col_idx = direction[1] + j
            if 0 <= row_idx < len(grid) and 0 <= col_idx < len(grid[0]):
                if grid[row_idx][col_idx] == "1":
                    grid[row_idx][col_idx] = 0
                    self.dfs(grid, row_idx, col_idx)


# @lc code=end


#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#
