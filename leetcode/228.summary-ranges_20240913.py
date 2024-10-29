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
        result = []
        left, right = 0, 1
        while right < len(nums):
            while right < len(nums) and nums[right] == nums[right - 1] + 1:
                right += 1
            if right == left + 1:
                result.append(f"{nums[left]}")
            else:
                result.append(f"{nums[left]}->{nums[right-1]}")
            left = right
            right = left + 1
        if left == len(nums) - 1:
            result.append(f"{nums[left]}")
        return result


# @lc code=end


#
# @lcpr case=start
# [0,1,2,4,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [0,2,3,4,6,8,9]\n
# @lcpr case=end

#
