"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-13 11:06:33
LastEditors: Helei.Yang
LastEditTime: 2025-01-13 11:45:09
FilePath: /magic_repo/leetcode/31.next-permutation_20250113.py
Description: 
"""

"""
Author: Helei.Yang
Email: helei_yang@zju.edu.cn
Date: 2025-01-13 11:06:33
LastEditors: Helei.Yang
LastEditTime: 2025-01-13 11:22:31
FilePath: /magic_repo/leetcode/31.next-permutation_20250113.py
Description:
"""

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
        if idx != -1:
            # 逆序找第一个大于 nums[idx] 的数
            jdx = len(nums) - 1
            while jdx > idx and nums[jdx] <= nums[idx]:
                jdx -= 1
            # 交换 nums[idx] 和 nums[jdx]
            nums[idx], nums[jdx] = nums[jdx], nums[idx]
        # 翻转 idx 后面的数组
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

