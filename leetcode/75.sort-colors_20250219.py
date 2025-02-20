#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30204
#
# [75] 颜色分类
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)

        p0 = -1
        p2 = n

        i = 0
        while i < p2:
            if nums[i] == 0:
                p0 += 1
                swap(i, p0)
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                p2 -= 1
                swap(i, p2)


# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

