#
# @lc app=leetcode.cn id=50 lang=python3
# @lcpr version=30204
#
# [50] Pow(x, n)
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        negative = n < 0
        n = abs(n)
        odd = n % 2 == 1
        half_res = self.myPow(x, n // 2)
        result = half_res * half_res * x if odd else half_res * half_res
        result = 1 / result if negative else result
        return result


# @lc code=end


#
# @lcpr case=start
# 2.00000\n10\n
# @lcpr case=end

# @lcpr case=start
# 2.10000\n3\n
# @lcpr case=end

# @lcpr case=start
# 2.00000\n-2\n
# @lcpr case=end

#
