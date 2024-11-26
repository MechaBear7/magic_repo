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

            # 检查中间值是否是目标值
            if nums[mid] == target:
                return mid

            # 判断左区间是否有序
            if nums[left] <= nums[mid]:
                # 目标值在左区间
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:  # 否则在右区间
                    left = mid + 1
            else:  # 右区间有序
                # 目标值在右区间
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:  # 否则在左区间
                    right = mid - 1

        # 如果找不到目标值
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
