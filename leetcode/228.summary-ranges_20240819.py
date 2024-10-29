#
# @lc app=leetcode.cn id=228 lang=python3
# @lcpr version=30204
#
# [228] 汇总区间
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        left_idx = 0
        right_idx = left_idx + 1
        while right_idx <= len(nums):
            while right_idx < len(nums) and nums[right_idx] == nums[right_idx - 1] + 1:
                right_idx += 1
            if right_idx == left_idx + 1:
                ans.append(f"{nums[left_idx]}")
            else:
                ans.append(f"{nums[left_idx]}->{nums[right_idx - 1]}")
            left_idx = right_idx
            right_idx = left_idx + 1

        return ans


# @lc code=end


#
# @lcpr case=start
# [0,1,2,4,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [0,2,3,4,6,8,9]\n
# @lcpr case=end

#
