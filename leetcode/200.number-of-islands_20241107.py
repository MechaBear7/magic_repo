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
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    cnt += 1
                    self.dfs(grid, i, j, "1", "0")
        return cnt

    def dfs(self, grid, i, j, src, tar):
        directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}
        for direction in directions:
            row, col = i + direction[0], j + direction[1]
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                if grid[row][col] == src:
                    grid[row][col] = tar
                    self.dfs(grid, row, col, src, tar)


# @lc code=end


#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#
