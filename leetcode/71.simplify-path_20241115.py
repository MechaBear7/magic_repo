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
        start = 0
        n = len(path)
        while start < n:
            while start < n and path[start] == "/":
                start += 1
            if start >= n:
                break
            end = start
            while end < n and path[end] != "/":
                end += 1
            dir_ = path[start:end]
            if dir_ == ".." and dirs:
                dirs.pop()
            elif dir_ != "." and dir_ != "..":
                dirs.append(dir_)
            start = end + 1
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
