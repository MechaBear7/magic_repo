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
        dirs = []
        temp = ""
        idx = 0
        while idx < len(path) and path[idx] == "/":
            idx += 1
        while idx < len(path):
            if path[idx] == "/":
                if temp == ".." and len(dirs) > 0:
                    dirs.pop()
                elif temp != ".." and temp != "." and temp != "":
                    dirs.append(temp)
                temp = ""
            else:
                temp += path[idx]
            idx += 1

        if temp == ".." and len(dirs) > 0:
            dirs.pop()
        elif temp != ".." and temp != "." and temp != "":
            dirs.append(temp)
        temp = ""

        return "/" + "/".join(dirs)


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
