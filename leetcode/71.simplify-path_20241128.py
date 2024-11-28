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
        word = ""
        idx = 0
        while idx < len(path) and path[idx] == "/":
            idx += 1
        while idx < len(path):
            if path[idx] == "/":
                if word == ".." and len(dirs) > 0:
                    dirs.pop()
                elif word != ".." and word != "." and len(word) > 0:
                    dirs.append(word)
                word = ""
            else:
                word += path[idx]
            idx += 1

        if word == ".." and len(dirs) > 0:
            dirs.pop()
        elif word != ".." and word != "." and len(word) > 0:
            dirs.append(word)

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
