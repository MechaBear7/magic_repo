#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30204
#
# [15] 三数之和
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if num > 0:
                return result
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + num == 0:
                    result.append([num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + num < 0:
                    left += 1
                else:
                    right -= 1
        return result


# @lc code=end


#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#
