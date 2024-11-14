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
        hashmap = {}
        for i in range(m):
            for j in range(n):
                if board[i][j] not in hashmap:
                    hashmap[board[i][j]] = [(i, j)]
                else:
                    hashmap[board[i][j]].append((i, j))

        for d in word:
            if d not in hashmap:
                return False

        directions = {(1, 0), (0, -1), (-1, 0), (0, 1)}

        def dfs(board, block, i, j, word, idx):
            if board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            for direction in directions:
                row, col = i + direction[0], j + direction[1]
                if 0 <= row < m and 0 <= col < n and not block[row][col]:
                    block[row][col] = True
                    if dfs(board, block, row, col, word, idx + 1):
                        return True
                    block[row][col] = False
            return False

        block = [[False for _ in range(n)] for _ in range(m)]
        for start_pos in hashmap[word[0]]:
            block[start_pos[0]][start_pos[1]] = True
            if dfs(board, block, start_pos[0], start_pos[1], word, 0):
                return True
            block[start_pos[0]][start_pos[1]] = False
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
