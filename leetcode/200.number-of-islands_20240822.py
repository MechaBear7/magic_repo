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
        num_row = len(grid)
        num_col = len(grid[0])
        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        directions = {(1, 0), (0, -1), (-1, 0), (0, 1)}
        for direction in directions:
            new_row = i + direction[0]
            new_col = j + direction[1]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] == "1":
                    grid[new_row][new_col] = "0"
                    self.dfs(grid, new_row, new_col)


# @lc code=end


#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#
