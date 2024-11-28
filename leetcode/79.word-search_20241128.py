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
        def dfs(board, masks, i, j, word, idx):
            if idx == len(word):
                return True

            directions = {(1, 0), (0, 1), (0, -1), (-1, 0)}
            for direction in directions:
                row = i + direction[0]
                col = j + direction[1]
                if 0 <= row < len(board) and 0 <= col < len(board[0]) and not masks[row][col] and word[idx] == board[row][col]:
                    masks[row][col] = True
                    if dfs(board, masks, row, col, word, idx + 1):
                        return True
                    masks[row][col] = False

        masks = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    masks[i][j] = True
                    if dfs(board, masks, i, j, word, 1):
                        return True
                    masks[i][j] = False
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
