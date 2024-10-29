#
# @lc app=leetcode.cn id=6 lang=python3
# @lcpr version=30204
#
# [6] Z 字形变换
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        store = [[] for _ in range(numRows)]
        flag = 0  # 0 or 1: 从上到下 或 从下到上
        idx = 0  # 数据往第 idx 行存放
        for d in s:
            store[idx].append(d)
            idx = idx + 1 if flag == 0 else idx - 1
            if idx == numRows - 1:
                flag = 1
            if idx == 0:
                flag = 0
        result = "".join(["".join(row_data) for row_data in store])
        print(store)
        return result


# @lc code=end


#
# @lcpr case=start
# "PAYPALISHIRING"\n3\n
# @lcpr case=end

# @lcpr case=start
# "PAYPALISHIRING"\n4\n
# @lcpr case=end

# @lcpr case=start
# "A"\n1\n
# @lcpr case=end

#
