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
        n = len(nums)
        if n == 0:
            return []
        result = []
        left_idx = 0
        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                if left_idx == i - 1:
                    result.append(f"{nums[left_idx]}")
                else:
                    result.append(f"{nums[left_idx]}->{nums[i-1]}")
                left_idx = i
        if left_idx == n - 1:
            result.append(f"{nums[left_idx]}")
        else:
            result.append(f"{nums[left_idx]}->{nums[-1]}")

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
