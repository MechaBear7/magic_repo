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
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result += 1
                    self.dfs(grid, i, j)
        return result

    def dfs(self, grid, i, j):
        directions = {(1, 0), (0, -1), (-1, 0), (0, 1)}
        for direction in directions:
            row, col = i + direction[0], j + direction[1]
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    self.dfs(grid, row, col)


# @lc code=end


#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#
