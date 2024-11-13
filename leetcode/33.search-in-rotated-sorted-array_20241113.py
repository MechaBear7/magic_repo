#
# @lc app=leetcode.cn id=33 lang=python3
# @lcpr version=30204
#
# [33] 搜索旋转排序数组
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:  # 左区间有序
                if nums[left] <= target and target < nums[mid]:  # target 在左区间
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 右区间有序
                if nums[mid] < target and target <= nums[right]:  # target 在右区间
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# @lc code=end


#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#
