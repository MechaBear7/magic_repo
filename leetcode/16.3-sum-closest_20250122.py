"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-22 16:47:42
LastEditors: Helei.Yang
LastEditTime: 2025-01-22 17:33:07
FilePath: /magic_repo/leetcode/16.3-sum-closest_20250122.py
Description: 
"""

#
# @lc app=leetcode.cn id=16 lang=python3
# @lcpr version=30204
#
# [16] 最接近的三数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == target:
                    return target
                else:
                    closest = cur_sum if abs(cur_sum - target) < abs(closest - target) else closest
                    if cur_sum < target:
                        left += 1
                    else:
                        right -= 1
        return closest

# @lc code=end



#
# @lcpr case=start
# [-1,2,1,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n1\n
# @lcpr case=end

#

