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
        ans = float("inf")
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(target - cur_sum) < abs(target - ans):
                    ans = cur_sum
                if cur_sum < target:
                    left += 1
                elif cur_sum == target:
                    return cur_sum
                else:
                    right -= 1
        return ans


# @lc code=end


#
# @lcpr case=start
# [-1,2,1,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n1\n
# @lcpr case=end

#
