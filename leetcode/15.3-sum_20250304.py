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
        nums.sort()
        result = []
        for idx in range(len(nums) - 2):
            if idx != 0 and nums[idx] == nums[idx - 1]:
                continue
            target = -nums[idx]
            left, right = idx + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[idx], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left, right = left + 1, right - 1
                elif nums[left] + nums[right] < target:
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

