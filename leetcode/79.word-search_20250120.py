"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-20 11:46:15
LastEditors: Helei.Yang
LastEditTime: 2025-01-20 16:30:28
FilePath: /magic_repo/leetcode/79.word-search_20250120.py
Description: 
"""
from typing import List

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
        directions = {(1, 0), (0, 1), (-1, 0), (0, -1)}

        def backtracking(board, masks, idx, jdx, word, i):
            if i >= len(word):
                return True
            if 0 <= idx < len(board) and 0 <= jdx < len(board[0]) and masks[idx][jdx] and board[idx][jdx] == word[i]:
                masks[idx][jdx] = False
                for direction in directions:
                    row, col = idx + direction[0], jdx + direction[1]
                    if backtracking(board, masks, row, col, word, i + 1):
                        return True
                masks[idx][jdx] = True
            return False
        
        masks = [[True for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtracking(board, masks, i, j, word, 0):
                    return True

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

