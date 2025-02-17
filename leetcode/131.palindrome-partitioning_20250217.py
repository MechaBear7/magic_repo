#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30204
#
# [131] 分割回文串
#
from typing import List

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        path = []
        result = []

        def check(i, j):
            # 检查 s[i, j]是否是回文串
            while i < j - 1:
                if s[i] != s[j - 1]:
                    return False
                i, j = i + 1, j - 1
            return True
        
        def dfs(start):
            if start == n:
                result.append(path[:])
                return

            for end in range(start + 1, n + 1):
                if check(start, end):
                    path.append(s[start:end])
                    dfs(end)
                    path.pop()
        
        dfs(0)
        
        return result
            
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.partition("aab"))
    print(solution.partition("a"))


#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#

