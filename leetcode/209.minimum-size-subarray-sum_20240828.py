#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30204
#
# [209] 长度最小的子数组
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums) + 1
        cumsum = 0
        left_idx = 0
        right_idx = 0
        while right_idx < len(nums):
            while right_idx < len(nums) and cumsum < target:
                cumsum += nums[right_idx]
                right_idx += 1
            while cumsum >= target:
                min_length = min(min_length, right_idx - left_idx)
                cumsum -= nums[left_idx]
                left_idx += 1
        return min_length if min_length != len(nums) + 1 else 0


# @lc code=end


#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#
