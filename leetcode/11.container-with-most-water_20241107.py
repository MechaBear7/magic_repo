#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30204
#
# [11] 盛最多水的容器
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        left_max, right_max = -float("inf"), -float("inf")
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            max_area = max(max_area, (right - left) * min(left_max, right_max))
            if left_max < right_max:
                left += 1
            else:
                right -= 1
        return max_area


# @lc code=end


#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#
