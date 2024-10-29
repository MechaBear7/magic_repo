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
        left2right = [1 for _ in range(n)]
        right2left = [1 for _ in range(n)]
        for i in range(1, n):
            left2right[i] = left2right[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right2left[i] = right2left[i + 1] * nums[i + 1]

        ans = [1 for _ in range(n)]
        for i in range(n):
            ans[i] = left2right[i] * right2left[i]
        return ans


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#
