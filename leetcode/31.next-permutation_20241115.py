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
        # 从后向前找第一个逆序数
        idx = len(nums) - 2
        while idx >= 0:
            if nums[idx] < nums[idx + 1]:
                break
            idx -= 1

        if idx == -1:
            left, right = 0, len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        else:
            # 从后向前找到第一个大于该数的数
            jdx = len(nums) - 1
            while jdx > idx:
                if nums[jdx] > nums[idx]:
                    nums[idx], nums[jdx] = nums[jdx], nums[idx]
                    break
                jdx -= 1
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
