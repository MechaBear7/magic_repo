#
# @lc app=leetcode.cn id=79 lang=python3
# @lcpr version=30204
#
# [79] 单词搜索
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        start_pos = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start_pos.append((i, j))

        if len(start_pos) == 0:
            return False

        def dfs(board, block, word, idx, pos):
            if idx == len(word):
                return True
            directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}
            for direction in directions:
                row, col = pos[0] + direction[0], pos[1] + direction[1]
                if 0 <= row < m and 0 <= col < n and not block[row][col]:
                    if board[row][col] == word[idx]:
                        block[row][col] = True
                        if dfs(board, block, word, idx + 1, (row, col)):
                            return True
                        block[row][col] = False
            return False

        block = [[False for _ in range(n)] for _ in range(m)]
        for pos in start_pos:
            block[pos[0]][pos[1]] = True
            if dfs(board, block, word, 1, pos):
                return True
            block[pos[0]][pos[1]] = False

        return False


# @lc code=end


#
# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"SEE"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCB"\n
# @lcpr case=end

#
