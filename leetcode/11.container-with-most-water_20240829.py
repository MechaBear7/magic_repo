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
        result = 0
        left_idx = 0
        right_idx = len(height) - 1
        while left_idx < right_idx:
            result = max(
                result,
                (right_idx - left_idx) * min(height[left_idx], height[right_idx]),
            )
            if height[left_idx] < height[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1
        return result


# @lc code=end


#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#
