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
        stk = []
        left, right = 0, len(path) - 1
        while left <= right:
            while left <= right and path[left] == "/":
                left += 1
            idx = left
            while idx <= right and path[idx] != "/":
                stk.append(path[idx])
                idx += 1
            if len(stk) != 0:
                sub_str = "".join(stk)
                if sub_str == ".." and dirs:
                    dirs.pop()
                elif sub_str != ".." and sub_str != ".":
                    dirs.append(sub_str)
                stk.clear()
            left = idx
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
