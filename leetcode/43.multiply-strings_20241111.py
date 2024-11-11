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
        ans = 0
        f1 = 1
        for i in range(len(num1) - 1, -1, -1):
            n1 = f1 * int(num1[i])
            f2 = 1
            for j in range(len(num2) - 1, -1, -1):
                n2 = f2 * int(num2[j])
                ans += n1 * n2
                f2 *= 10
            f1 *= 10
        return str(ans)


# @lc code=end


#
# @lcpr case=start
# "2"\n"3"\n
# @lcpr case=end

# @lcpr case=start
# "123"\n"456"\n
# @lcpr case=end

#
