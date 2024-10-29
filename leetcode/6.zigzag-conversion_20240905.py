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
        row_data = [[] for _ in range(numRows)]
        flag = 0  # 0 代表从上到下
        row_idx = 0  # 当前应该往第几行填充数据
        for d in s:
            row_data[row_idx].append(d)
            row_idx = row_idx + 1 if flag == 0 else row_idx - 1
            if row_idx == 0:
                flag = 0
            elif row_idx == numRows - 1:
                flag = 1
        result = "".join(["".join(row_info) for row_info in row_data])
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
