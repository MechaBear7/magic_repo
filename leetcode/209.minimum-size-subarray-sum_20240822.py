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
        res = len(nums) + 1
        sub_sum = 0
        left_idx = 0
        right_idx = 0
        while right_idx < len(nums):
            sub_sum += nums[right_idx]
            while sub_sum >= target:
                res = min(res, right_idx - left_idx + 1)
                sub_sum -= nums[left_idx]
                left_idx += 1
            right_idx += 1
        return res if res != len(nums) + 1 else 0


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
