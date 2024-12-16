#
# @lc app=leetcode.cn id=LCR 135 lang=python3
# @lcpr version=30204
#
# [LCR 135] 报数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countNumbers(self, cnt: int) -> List[int]:
        result = []
        i = 1
        while i != 10**cnt:
            result.append(i)
            i += 1
        return result


# @lc code=end


#
# @lcpr case=start
# 2\n
# @lcpr case=end

#
