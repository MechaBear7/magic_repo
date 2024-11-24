#
# @lc app=leetcode.cn id=152 lang=python3
# @lcpr version=30204
#
# [152] 乘积最大子数组
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_nums = [0 for _ in range(n)]
        max_nums = [0 for _ in range(n)]
        min_nums[0], max_nums[0] = nums[0], nums[0]
        for i in range(1, n):
            min_nums[i] = min(min_nums[i - 1] * nums[i], max_nums[i - 1] * nums[i], nums[i])
            max_nums[i] = max(min_nums[i - 1] * nums[i], max_nums[i - 1] * nums[i], nums[i])
        return max(max_nums)


# @lc code=end


#
# @lcpr case=start
# [2,3,-2,4]\n
# @lcpr case=end

# @lcpr case=start
# [-2,0,-1]\n
# @lcpr case=end

#
