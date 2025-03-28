#
# @lc app=leetcode.cn id=287 lang=python3
# @lcpr version=30204
#
# [287] 寻找重复数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            cnts = sum(left <= num <= mid for num in nums)
            if cnts > mid - left + 1:
                right = mid
            else:
                left = mid + 1
        return left


# @lc code=end


#
# @lcpr case=start
# [1,3,4,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,3]\n
# @lcpr case=end

#
