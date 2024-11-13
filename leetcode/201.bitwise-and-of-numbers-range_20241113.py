#
# @lc app=leetcode.cn id=201 lang=python3
# @lcpr version=30204
#
# [201] 数字范围按位与
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        # 找到left和right的公共前缀，并统计这个过程右移了多少次
        while left != right:
            cnt += 1
            left = left >> 1
            right = right >> 1
        # 将这个公共前缀还原回去
        return (left & right) << cnt


# @lc code=end


#
# @lcpr case=start
# 5\n7\n
# @lcpr case=end

# @lcpr case=start
# 0\n0\n
# @lcpr case=end

# @lcpr case=start
# 1\n2147483647\n
# @lcpr case=end

#
