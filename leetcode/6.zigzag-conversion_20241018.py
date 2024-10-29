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
        result = [[] for _ in range(numRows)]
        cur_row = 0
        top2bottom = True
        for elem in s:
            result[cur_row].append(elem)
            if top2bottom:
                cur_row += 1
            else:
                cur_row -= 1
            if cur_row == 0:
                top2bottom = True
            elif cur_row == numRows - 1:
                top2bottom = False
        result_str = "".join("".join(row_data) for row_data in result)
        return result_str


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
