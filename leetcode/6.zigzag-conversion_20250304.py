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
        row_idx = 0
        top2bottom = True
        for d in s:
            row_data[row_idx].append(d)
            if top2bottom:
                row_idx += 1
                if row_idx == numRows - 1:
                    top2bottom = False
            else:
                row_idx -= 1
                if row_idx == 0:
                    top2bottom = True
        
        return "".join(["".join(data) for data in row_data])


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

