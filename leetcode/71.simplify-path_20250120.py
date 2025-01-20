"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-20 11:07:44
LastEditors: Helei.Yang
LastEditTime: 2025-01-20 11:44:47
FilePath: /magic_repo/leetcode/71.simplify-path_20250120.py
Description: 
"""

#
# @lc app=leetcode.cn id=71 lang=python3
# @lcpr version=30204
#
# [71] 简化路径
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        idx = 0
        while idx < len(path) and path[idx] != "/":
            idx += 1
        idx += 1
        sub_path = ""
        while idx <= len(path):
            if idx == len(path) or path[idx] == "/":
                if sub_path == ".." and len(result) > 0:
                    result.pop()
                elif sub_path not in ["", ".", ".."]:
                    result.append(sub_path)
                sub_path = ""
            else:
                sub_path += path[idx]
            idx += 1
        return "/" + "/".join(result)

            
# @lc code=end



#
# @lcpr case=start
# "/home/"\n
# @lcpr case=end

# @lcpr case=start
# "/home//foo/"\n
# @lcpr case=end

# @lcpr case=start
# "/home/user/Documents/../Pictures"\n
# @lcpr case=end

# @lcpr case=start
# "/../"\n
# @lcpr case=end

# @lcpr case=start
# "/.../a/../b/c/../d/./"\n
# @lcpr case=end

#

