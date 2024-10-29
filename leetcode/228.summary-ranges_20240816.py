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
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        res = []
        left_idx = 0
        for right_idx in range(1, len(nums)):
            if nums[right_idx] != nums[right_idx - 1] + 1:
                if right_idx == left_idx + 1:
                    res.append(f"{nums[left_idx]}")
                else:
                    res.append(f"{nums[left_idx]}->{nums[right_idx - 1]}")
                left_idx = right_idx

        if left_idx == right_idx:
            res.append(f"{nums[left_idx]}")
        else:
            res.append(f"{nums[left_idx]}->{nums[right_idx]}")

        return res


# @lc code=end


#
# @lcpr case=start
# [0,1,2,4,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [0,2,3,4,6,8,9]\n
# @lcpr case=end

#
