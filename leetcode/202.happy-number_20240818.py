#
# @lc app=leetcode.cn id=202 lang=python3
# @lcpr version=30204
#
# [202] 快乐数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        store = set()
        ans = n
        while ans != 1:
            store.add(ans)
            temp = ans
            ans = 0
            while temp > 0:
                num = temp % 10
                temp = temp // 10
                ans += num * num
            if ans in store:
                return False
        return True


# @lc code=end


#
# @lcpr case=start
# 19\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#
