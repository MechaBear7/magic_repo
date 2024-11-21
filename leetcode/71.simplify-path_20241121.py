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
        left, end = 0, len(path) - 1
        while left < end:
            while left < end and path[left] == "/":
                left += 1
            if left > end:
                break
            temp = ""
            right = left
            while right <= end and path[right] != "/":
                temp += path[right]
                right += 1
            if len(temp) > 0:
                if temp == ".." and len(dirs) != 0:
                    dirs.pop()
                elif temp != ".." and temp != ".":
                    dirs.append(temp)
            left = right

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
