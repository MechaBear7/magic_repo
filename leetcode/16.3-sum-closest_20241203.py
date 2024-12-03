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
        result = float("inf")
        for idx in range(len(nums)):
            left, right = idx + 1, len(nums) - 1
            while left < right:
                cur_sum = nums[idx] + nums[left] + nums[right]
                if cur_sum == target:
                    return target
                else:
                    result = cur_sum if abs(cur_sum - target) < abs(result - target) else result
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
