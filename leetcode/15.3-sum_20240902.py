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
        nums = sorted(nums)
        result = []
        search_idx = 0
        while search_idx < len(nums):
            while (
                search_idx != 0
                and search_idx < len(nums)
                and nums[search_idx] == nums[search_idx - 1]
            ):
                search_idx += 1
            left_idx = search_idx + 1
            right_idx = len(nums) - 1
            while left_idx < right_idx:
                if nums[search_idx] + nums[left_idx] + nums[right_idx] == 0:
                    result.append([nums[search_idx], nums[left_idx], nums[right_idx]])
                    while left_idx < right_idx and nums[left_idx] == nums[left_idx + 1]:
                        left_idx += 1
                    while (
                        left_idx < right_idx and nums[right_idx] == nums[right_idx - 1]
                    ):
                        right_idx -= 1
                    left_idx, right_idx = left_idx + 1, right_idx - 1
                elif nums[search_idx] + nums[left_idx] + nums[right_idx] < 0:
                    left_idx += 1
                else:
                    right_idx -= 1
            search_idx += 1
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
