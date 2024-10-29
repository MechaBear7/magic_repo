#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30204
#
# [238] 除自身以外数组的乘积
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l2r = [1 for _ in range(n)]
        r2l = [1 for _ in range(n)]

        for i in range(n):
            if i != 0:
                l2r[i] = nums[i-1] * l2r[i-1]
        for i in reversed(range(n)):
            if i != n - 1:
                r2l[i] = nums[i+1] * r2l[i+1]
        
        res = []
        for i in range(n):
            res.append(l2r[i] * r2l[i])
        return res

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#

