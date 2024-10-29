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
        total_sum = 0
        hashmap = {}
        for idx, num in enumerate(nums):
            if idx == 0:
                hashmap[idx] = 0
            else:
                hashmap[idx] = hashmap[idx-1] + nums[idx-1]
            total_sum += num
        for idx in range(len(nums)):
            if hashmap[idx] == total_sum - nums[idx] - hashmap[idx]:
                return idx
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

