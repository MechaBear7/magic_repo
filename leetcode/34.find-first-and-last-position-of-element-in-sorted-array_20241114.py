#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30204
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                l, r = mid, mid
                while l >= 0 and nums[l] == target:
                    l -= 1
                while r < len(nums) and nums[r] == target:
                    r += 1
                return [l + 1, r - 1]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]


# @lc code=end


#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#
