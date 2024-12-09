#
# @lc app=leetcode.cn id=43 lang=python3
# @lcpr version=30204
#
# [43] 字符串相乘
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        m, n = len(num1), len(num2)
        f1 = 1
        for i in range(m - 1, -1, -1):
            f2 = 1
            for j in range(n - 1, -1, -1):
                result += f1 * int(num1[i]) * f2 * int(num2[j])
                f2 *= 10
            f1 *= 10
        return str(result)


# @lc code=end


#
# @lcpr case=start
# "2"\n"3"\n
# @lcpr case=end

# @lcpr case=start
# "123"\n"456"\n
# @lcpr case=end

#
