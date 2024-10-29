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
        slow_idx, fast_idx = 0, 0
        cumsum = 0
        while fast_idx < len(nums):
            while cumsum < target and fast_idx < len(nums):
                cumsum += nums[fast_idx]
                fast_idx += 1
            while cumsum >= target:
                min_length = min(min_length, fast_idx - slow_idx)
                cumsum -= nums[slow_idx]
                slow_idx += 1
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
