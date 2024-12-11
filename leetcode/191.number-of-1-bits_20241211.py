#
# @lc app=leetcode.cn id=191 lang=python3
# @lcpr version=30204
#
# [191] 位1的个数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnts = 0
        while n > 0:
            cnts += n & 1
            n = n // 2
        return cnts


# @lc code=end


#
# @lcpr case=start
# 11\n
# @lcpr case=end

# @lcpr case=start
# 128\n
# @lcpr case=end

# @lcpr case=start
# 2147483645\n
# @lcpr case=end

#
