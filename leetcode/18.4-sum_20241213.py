#
# @lc app=leetcode.cn id=18 lang=python3
# @lcpr version=30204
#
# [18] 四数之和
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        for idx in range(n):
            if idx != 0 and nums[idx] == nums[idx - 1]:
                continue
            for jdx in range(idx + 1, n):
                if jdx != idx + 1 and nums[jdx] == nums[jdx - 1]:
                    continue
                cur_target = target - nums[idx] - nums[jdx]
                left, right = jdx + 1, n - 1
                while left < right:
                    if nums[left] + nums[right] == cur_target:
                        result.append([nums[idx], nums[jdx], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left, right = left + 1, right - 1
                    elif nums[left] + nums[right] < cur_target:
                        left += 1
                    else:
                        right -= 1
        return result


# @lc code=end


#
# @lcpr case=start
# [1,0,-1,0,-2,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n8\n
# @lcpr case=end

#
