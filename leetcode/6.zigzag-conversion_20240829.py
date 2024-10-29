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
        result = ""
        loop_step = (numRows - 1) * 2
        for i in range(numRows):
            search_idx = i
            step = (numRows - i - 1) * 2
            while search_idx < len(s):
                if step != 0:
                    result = result + s[search_idx]
                search_idx += step
                if step < loop_step:
                    step = loop_step - step
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
