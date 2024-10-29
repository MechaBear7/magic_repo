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
        cumsum = []
        for idx, num in enumerate(nums):
            if idx == 0:
                cumsum.append(num)
            else:
                cumsum.append(cumsum[idx-1] + num)
        for idx, num in enumerate(nums):
            if cumsum[idx] - num == cumsum[-1] - cumsum[idx]:
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

