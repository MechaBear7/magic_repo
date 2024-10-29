#
# @lc app=leetcode.cn id=724 lang=python3
# @lcpr version=30204
#
# [724] 寻找数组的中心下标
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        list_sum = [0 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            list_sum[i] = list_sum[i - 1] + nums[i - 1]
        total_sum = list_sum[-1] + nums[-1]
        for i in range(len(nums)):
            if list_sum[i] == total_sum - list_sum[i] - nums[i]:
                return i
        return -1


# @lc code=end


#
# @lcpr case=start
# [1, 7, 3, 6, 5, 6]\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 3]\n
# @lcpr case=end

# @lcpr case=start
# [2, 1, -1]\n
# @lcpr case=end

#
