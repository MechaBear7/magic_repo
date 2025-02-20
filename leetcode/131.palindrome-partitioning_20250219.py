#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30204
#
# [131] 分割回文串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def check(i, j):
            while i < j - 1:
                if s[i] != s[j - 1]:
                    return False
                i, j = i + 1, j - 1
            return True
        
        def dfs(start):
            if start == len(s):
                result.append(path[:])
                return
            
            for end in range(start, len(s)):
                if check(start, end+1):
                    path.append(s[start:end+1])
                    dfs(end+1)
                    path.pop()
        
        dfs(0)
        return result

# @lc code=end



#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#

