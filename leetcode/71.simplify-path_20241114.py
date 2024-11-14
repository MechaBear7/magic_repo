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
        dirs = []  # 双端队列，存储最终简化后的路径
        start = 0  # 目录名起点
        n = len(path)
        while start < n:
            while start < n and path[start] == "/":
                start += 1  # 找到目录名的起点，为首个不为'/'的字符
            if start >= n:
                break  # 起点越界，遍历结束
            end = start  # 目录名的终点，初始为起点
            while end < n and path[end] != "/":
                end += 1  # 找到目录名的终点，为首个'/'字符
            dir_ = path[start:end]  # 截取目录名
            if dir_ == ".." and dirs:
                dirs.pop()  # 如果目录名是返回上一级，那么就从队尾弹出一个目录名
            elif dir_ != "." and dir_ != "..":
                dirs.append(dir_)  # 如果目录名不为.或..，那么就加入队尾，组成路径
            start = end  # 目录起点更新为终点，寻找下一个目录名
        return "/" + "/".join(dirs)  # 以单斜杠为分隔符拼接目录名成新路径，开头再加上'/'


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
