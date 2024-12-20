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
        result = float("inf")
        nums.sort()
        for idx in range(len(nums)):
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                if nums[idx] + nums[left] + nums[right] == target:
                    return target
                else:
                    cur_sum = nums[idx] + nums[left] + nums[right]
                    if abs(target - cur_sum) < abs(result - target):
                        result = cur_sum
                    if cur_sum < target:
                        left += 1
                    else:
                        right -= 1

        return result


# @lc code=end


#
# @lcpr case=start
# [-1,2,1,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n1\n
# @lcpr case=end

#
