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
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur == target:
                    return target
                else:
                    if abs(target - cur) < abs(target - result):
                        result = cur
                    if nums[i] + nums[left] + nums[right] < target:
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
