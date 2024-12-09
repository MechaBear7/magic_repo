#
# @lc app=leetcode.cn id=31 lang=python3
# @lcpr version=30204
#
# [31] 下一个排列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = len(nums) - 2
        while idx >= 0 and nums[idx] >= nums[idx + 1]:
            idx -= 1

        # 如果找到了这样的元素
        if idx >= 0:
            jdx = len(nums) - 1
            # 找到第一个大于 nums[idx] 的元素
            while jdx > idx and nums[jdx] <= nums[idx]:
                jdx -= 1
            # 交换 nums[idx] 和 nums[jdx]
            nums[idx], nums[jdx] = nums[jdx], nums[idx]

        left, right = idx + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,5]\n
# @lcpr case=end

#
