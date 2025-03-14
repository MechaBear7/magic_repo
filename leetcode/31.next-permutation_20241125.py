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
        n = len(nums)
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        j = n - 1
        if i != -1:
            while j > i:
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j -= 1

        left, right = i + 1, len(nums) - 1
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
