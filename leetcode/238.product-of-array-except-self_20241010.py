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
        for i in range(1, n):
            l2r[i] = l2r[i - 1] * nums[i - 1]
        for i in reversed(range(0, n - 1)):
            r2l[i] = r2l[i + 1] * nums[i + 1]
        result = []
        for i in range(n):
            result.append(l2r[i] * r2l[i])
        return result


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#
